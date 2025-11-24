import json
import os
import random
import msvcrt
import sys
from datetime import datetime

# Database file
DB = "bank_data.json"

class Bank:
    def __init__(self):
        self.d = self.load() # d = data
        self.c = None        # c = current user id

    def load(self):
        if os.path.exists(DB):
            try:
                with open(DB, "r") as f: return json.load(f)
            except: return {}
        return {}

    def save(self):
        with open(DB, "w") as f: json.dump(self.d, f, indent=4)

    # Function to show '*' while typing
    def get_pass(self, prompt="PIN: "):
        print(prompt, end='', flush=True)
        buf = ""
        while True:
            ch = msvcrt.getch()
            if ch in {b'\r', b'\n'}: # Enter key
                print('')
                break
            elif ch == b'\x08': # Backspace
                if len(buf) > 0:
                    buf = buf[:-1]
                    print('\b \b', end='', flush=True)
            else:
                try:
                    buf += ch.decode('utf-8')
                    print('*', end='', flush=True)
                except: pass
        return buf

    def log(self, uid, msg):
        t = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.d[uid]["history"].append(f"[{t}] {msg}")

    def reg(self):
        print("\n--- NEW ACCOUNT ---")
        n = input("Full Name: ")
        while True:
            p = self.get_pass("Set 4-Digit PIN: ")
            if len(p) == 4 and p.isdigit(): break
            print("PIN must be 4 numbers.")
        
        qs = ["Pet name?", "Mom's maiden name?", "Birth city?", "Fav food?", "First school?"]
        for i, q in enumerate(qs, 1): print(f"{i}. {q}")
        
        try: x = int(input("Pick Question (1-5): ")) - 1
        except: x = 0
        q_sel = qs[x] if 0 <= x < 5 else qs[0]
        
        ans = input("Answer: ").lower()
        
        # Generate ID
        id = str(random.randint(10000, 99999))
        while id in self.d: id = str(random.randint(10000, 99999))

        self.d[id] = {"name": n, "pin": p, "bal": 0.0, "sq": q_sel, "sa": ans, "history": []}
        self.save()
        print(f"Done! Your ID is: {id}")
        input("Hit Enter...")

    def forgot(self):
        print("\n--- RESET PIN ---")
        id = input("Account ID: ")
        if id not in self.d:
            print("Not found.")
            return
        
        u = self.d[id]
        print(f"Question: {u['sq']}")
        a = input("Answer: ").lower()
        
        if a == u['sa']:
            np = self.get_pass("New PIN: ")
            if len(np) == 4 and np.isdigit():
                u['pin'] = np
                self.save()
                print("PIN changed.")
            else: print("Invalid PIN.")
        else: print("Wrong answer.")
        input("Hit Enter...")

    def trans(self):
        try:
            tid = input("Target ID: ")
            amt = float(input("Amount: "))
            
            if tid not in self.d: print("Target not found."); return
            if tid == self.c: print("Can't transfer to self."); return
            if amt > self.d[self.c]["bal"]: print("Low funds."); return
            
            # Transfer logic
            s_name = self.d[self.c]["name"] # sender
            r_name = self.d[tid]["name"]    # receiver
            
            self.d[self.c]["bal"] -= amt
            self.d[tid]["bal"] += amt
            
            self.log(self.c, f"Transfer to {r_name} ({tid}): -{amt}")
            self.log(tid, f"From {s_name} ({self.c}): +{amt}")
            self.save()
            print("Transfer Success.")
        except: print("Error in input.")
        input("Hit Enter...")

    def home(self):
        while self.c:
            os.system('cls')
            u = self.d[self.c]
            print(f"WELCOME {u['name']}")
            print(f"ID: {self.c} | Balance: {u['bal']}")
            print("-" * 30)
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. History")
            print("5. Logout")
            
            opt = input("Choice: ")
            
            if opt == '1':
                try:
                    a = float(input("Amount: "))
                    if a > 0:
                        u['bal'] += a
                        self.log(self.c, f"Deposit: +{a}")
                        self.save()
                        print("Deposited.")
                except: pass
            elif opt == '2':
                try:
                    a = float(input("Amount: "))
                    if 0 < a <= u['bal']:
                        u['bal'] -= a
                        self.log(self.c, f"Withdraw: -{a}")
                        self.save()
                        print("Withdrawn.")
                    else: print("Invalid or low balance.")
                except: pass
            elif opt == '3': self.trans()
            elif opt == '4':
                print("\nLast Transactions:")
                for h in u['history'][-7:]: print(h)
                input("\nHit Enter...")
            elif opt == '5': self.c = None; return
            
            if opt in ['1', '2']: input("Hit Enter...")

    def main(self):
        while True:
            os.system('cls')
            print("=== VIT BANK (VITyarthi) ===")
            print("1. Login")
            print("2. Create Account")
            print("3. Forgot PIN")
            print("4. Exit")
            
            ch = input("Select: ")
            
            if ch == '1':
                id = input("ID: ")
                p = self.get_pass()
                if id in self.d and self.d[id]['pin'] == p:
                    self.c = id
                    self.home()
                else:
                    print("Wrong ID or PIN")
                    input()
            elif ch == '2': self.reg()
            elif ch == '3': self.forgot()
            elif ch == '4':
                print("\nBuild By : Pratha Chouhan")
                print("Reg No. 25BAI10470")
                break

if __name__ == "__main__":
    Bank().main()