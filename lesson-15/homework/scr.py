import sqlite3
 
conn = sqlite3.connect('homework.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Roster(
        name TEXT,
        Species TEXT,
        age INT
    )
""")
conn.commit()
conn.close()

 
with sqlite3.connect('homework.db') as conn:
    cursor = conn.cursor()
    a = [
        ('Benjamin Sisko','Human', 40),
        ('Jadzia Dax','Trill', 300),
        ('Kira Nerys','Bajoran',29)
    ]
    
    cursor.executemany('INSERT INTO Roster(name, Species, age) VALUES(?, ?, ?)', a)

     
    cursor.execute('UPDATE Roster SET name = ? WHERE name = ?', ('Ezri Dax', 'Jadzia Dax'))

 
    cursor.execute("SELECT name, age FROM Roster WHERE Species = 'Bajoran'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
