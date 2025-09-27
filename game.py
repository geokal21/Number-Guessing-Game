import random

def number_guessing_game():
     print ("🎲 Καλωσήρθες στο Number Guessing Game!")
     print ("Έχω διαλέξει έναν αριθμό από το 1 έως το 100. Μπορείς να τον μαντέψεις;")

     # Ο υπολογιστής επιλέγει τυχαίο αριθμό
     secret_number = random.randint(1, 100)
     attempts = 0
     guess = None

     while guess != secret_number:
         try:
             guess = int(input("Δώσε έναν αριθμό: "))
             attempts += 1

             if guess < secret_number:
                 print("🔽 Πολύ μικρός! Δοκίμασε ξανά.")
             elif guess > secret_number:
                 print("🔼 Πολύ μεγάλος! Δοκίμασε ξανά.")
             else:
                 print(f"🎉 Μπράβο! Βρήκες τον αριθμό {secret_number} σε {attempts} προσπάθειες.")
         except valueError:
             print("⚠️ Δώσε έναν έγκυρο αριθμό.")

# Εκτέλση παιχνιδιού
number_guessing_game()