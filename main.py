
import sqlite3
import os
import click


filename = "leerlingen.sqlite3"
if (os.path.exists(filename)):
    os.remove(filename)
conn = sqlite3.connect(filename)
c = conn.cursor()
c.execute('''CREATE TABLE Leerlingen (ID INTEGER PRIMARY KEY, Voornaam text, Achternaam text)''')


# Hard-coded toegevoegd
c.execute("""INSERT INTO Leerlingen(Voornaam, Achternaam) VALUES (?,?);""",
          ("Joske", "Meylemans"))
c.execute("""INSERT INTO Leerlingen(Voornaam, Achternaam) VALUES (?,?);""",
          ("Arne", "Pinnemuts"))
c.execute("""INSERT INTO Leerlingen(Voornaam, Achternaam) VALUES (?,?);""",
          ("Arne", "Van Den Banus"))
# Save (commit) the changes
conn.commit()

print("Letter:")
letter = click.getchar()

while letter != "S":
    print(letter)
    if letter == "N":
        vname = input("Voornaam: ")
        aname = input("Achternaam: ")
        c.execute(
            f"""INSERT INTO Leerlingen(Voornaam, Achternaam) VALUES (?,?)""", (vname, aname))
    elif letter == "V":
        for lln in c.execute('SELECT * FROM Leerlingen ORDER BY Voornaam ASC'):
            print(lln[1] + " " + lln[2])
    elif letter == "V":
        for lln in c.execute('SELECT * FROM Leerlingen ORDER BY Achternaam ASC'):
            print(lln[1] + " " + lln[2])
    elif letter == "X":
        id = (input("ID: "),)
        c.execute(f'DELETE FROM Leerlingen WHERE ID=', id)
    elif letter == "D":
        voornaam = (input("Voornaam: "),)
        lln = c.execute(
            f'SELECT * FROM Leerlingen WHERE Voornaam=?', voornaam).fetchall()

        # Als er meer lln met dezelfde voornaam zijn, moet ge maar is bekijke

        # geen lln met dezelfde voornaam
        # else:
        c.execute('DELETE FROM Leerlingen WHERE Voornaam={voornaam}')

    conn.commit()
    print("Actie:")
    letter = click.getchar().upper()
