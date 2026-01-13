

C_FILE = "ctemps.txt"
F_FILE = "ftemps.txt"


try:
    with open(C_FILE, "r") as c_file, open(F_FILE, "w") as f_file:
        c_temps = [line.rstrip() for line in c_file]

        for temperature in c_temps:

            f_temp = float(temperature) * (9/5) + 32

            f_file.write(f"{f_temp}\n")

            print(f"{temperature} Celcius is {f_temp} Fahrenheit")

except Exception as e:
    print(f"You had a file exception man. {e}")