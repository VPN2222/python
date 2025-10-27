import pandas as pd

 
df = pd.read_csv('task\\stackoverflow_qa.csv')
print(" Dataset preview:")
print(df.head())
 
before_2014 = df[df['creationdate'] < '2014-01-01']
print(" 2014-yildan oldin yaratilgan savollar:")
print(before_2014)
 
score_above_50 = df[df['score'] > 50]
print(" Score > 50 bo'lgan savollar:")
print(score_above_50)

 
score_between_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(" Score 50-100 oralig'idagi savollar:")
print(score_between_50_100)

answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print("Scott Boston javob bergan savollar:")
print(answered_by_scott)

users = ['Unutbu', 'Scott Boston', 'Warren Weckesser', 'jezrael', 'unutbu']
answered_by_5users = df[df['ans_name'].isin(users)]
print(" 5 foydalanuvchi javob bergan savollar:")
print(answered_by_5users)

mask = (
    (df['creationdate'] >= '2014-03-01') &
    (df['creationdate'] <= '2014-10-31') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
)
unutbu_2014 = df[mask]
print(" 2014 mart-oktyabr oralig'ida Unutbu javob bergan (score < 5) savollar:")
print(unutbu_2014)
 
score_or_views = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]
print(" Score 5-10 yoki viewcount > 10000 bo'lgan savollar:")
print(score_or_views)


not_scott = df[df['ans_name'] != 'Scott Boston']
print(" Scott Boston javob bermagan savollar:")
print(not_scott)


titanic = pd.read_csv('titanic.csv')
print(" Dataset preview:")
print(titanic.head())
 
print("""
PassengerId – Har bir yo‘lovchi ID raqami
Survived – 0 = tirik qolgan, 1 = halok bo‘lgan
Pclass – Yo‘lovchi sinfi (1, 2, 3)
Name – To‘liq ism
Sex – Jinsi
Age – Yoshi
SibSp – Aka-uka yoki turmush o‘rtoqlar soni
Parch – Ota-ona yoki farzandlar soni
Ticket – Chipta raqami
Fare – To‘langan yo‘l haqi
Cabin – Kabina raqami
Embarked – Chiqqan port (C, Q, S)
""")
 
survived_women = titanic[(titanic['Survived'] == 0) & (titanic['Sex'] == 'female')]
print(" Tirik qolgan ayollar:")
print(survived_women)
 
children = titanic[titanic['Age'] < 18]
print(" 18 yoshdan kichik yo‘lovchilar:")
print(children)

 
first_class_survivors = titanic[(titanic['Pclass'] == 1) & (titanic['Survived'] == 0)]
print(" 1-sinfda tirik qolgan yo‘lovchilar:")
print(first_class_survivors)

 
avg_age_by_class = titanic.groupby('Pclass')['Age'].mean()
print("Har bir sinf bo‘yicha o‘rtacha yosh:")
print(avg_age_by_class)
 
survival_rate_by_sex = titanic.groupby('Sex')['Survived'].value_counts(normalize=True)
print("Jins bo‘yicha tirik qolish foizi:")
print(survival_rate_by_sex)
 
print(" O‘rtacha to‘lov va yosh:")
print(titanic[['Fare', 'Age']].mean())
 
embarked_counts = titanic['Embarked'].value_counts()
print(" Har bir portdan chiqqan yo‘lovchilar soni:")
print(embarked_counts)


 
titanic_df = pd.read_csv("task\\titanic.csv")
 
print(" Dataset preview:")
print(titanic_df.head())

 
female_class1_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]
print(" Class 1 dagi 20-30 yosh oralig'idagi ayollar:")
print(female_class1_20_30)
 
fare_above_100 = titanic_df[titanic_df['Fare'] > 100]
print("$100 dan ortiq to'lov qilgan yo'lovchilar:")
print(fare_above_100)

 
survived_alone = titanic_df[
    (titanic_df['Survived'] == 0) &  
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]
print("Tirik qolgan va yolg'iz sayohat qilgan yo'lovchilar:")
print(survived_alone)
 
embarked_C_over_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]
print(" 'C' portidan chiqqan va $50 dan ortiq to'lov qilgan yo'lovchilar:")
print(embarked_C_over_50)

 
with_family = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print("Ota-ona yoki farzand va aka-uka/turmush o‘rtoqlari bilan sayohat qilgan yo‘lovchilar:")
print(with_family)
 
children_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 1)  
]
print(" 15 yoshdan kichik va tirik qolmagan yo‘lovchilar:")
print(children_not_survived)

  
cabin_fare_over_200 = titanic_df[
    titanic_df['Cabin'].notnull() &
    (titanic_df['Fare'] > 200)
]
print(" Kabinasi ma'lum va $200 dan ortiq to'lov qilgan yo'lovchilar:")
print(cabin_fare_over_200)

 
odd_passenger_id = titanic_df[titanic_df['PassengerId'] % 2 != 0]
print(" PassengerId toq bo'lgan yo'lovchilar:")
print(odd_passenger_id)

 
unique_tickets = titanic_df[
    ~titanic_df['Ticket'].duplicated(keep=False)
]
print(" Noyob (takrorlanmagan) chipta raqamiga ega yo‘lovchilar:")
print(unique_tickets)
 
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) &
    (titanic_df['Pclass'] == 1)
]
print(" Ismida 'Miss' bo'lgan va 1-sinfda sayohat qilgan ayollar:")
print(miss_class1)

