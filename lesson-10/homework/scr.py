class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status    
    
    def mark_complete(self):
        self.status = "Complete"

class ToDoList:
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def see_all_tasks(self):
        if not self.task_list:
            print("No tasks found.")
        else:
            for i, t in enumerate(self.task_list, 1):
                print(f"{i}. Title: {t.title} | Due: {t.due_date} | Status: {t.status}")

    def display_incomplete_tasks(self):
        has_incomplete = False
        for task in self.task_list:
            if task.status != "Complete":
                print(f"Incomplete → {task.title}")
                has_incomplete = True
        if not has_incomplete:
            print(" All tasks are complete!")

    def mark_task_complete(self, task_index):
        """Tanlangan taskni bajarilgan deb belgilaydi"""
        if 0 <= task_index < len(self.task_list):
            self.task_list[task_index].mark_complete()
            print(f"True'{self.task_list[task_index].title}' marked as complete!")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()

    while True:
        print("\n=== ToDo List Menu ===")
        print("1.  Add Task")
        print("2.  Mark Task as Complete")
        print("3.  List All Tasks")
        print("4.  Display Incomplete Tasks")
        print("5.  Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print(" Task added successfully!")
        elif choice == "2":
            todo.see_all_tasks()
            try:
                task_num = int(input("Enter task number to mark complete: ")) - 1
                todo.mark_task_complete(task_num)
            except ValueError:
                print(" Please enter a valid number.")

        elif choice == "3":
            todo.see_all_tasks()

        elif choice == "4":
            todo.display_incomplete_tasks()

        elif choice == "5":
            print(" Exiting program... Goodbye!")
            break

        else:
            print(" Invalid choice. Please select 1-5.")
 
 
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.post_list = []

    def add_post(self, post):
        self.post_list.append(post)
        print(f"Post '{post.title}' added successfully!")

    def see_all_posts(self):
        if not self.post_list:
            print("No posts available.")
        else:
            print("\n All Posts:")
            for i, p in enumerate(self.post_list, 1):
                print(f"{i}. Title: {p.title} | Author: {p.author} | Content: {p.content}")

    def display_posts_by_author(self):
        a = input("Enter author name: ")
        found = False
        print(f"\n Posts by {a}:")
        for p in self.post_list:
            if p.author.lower() == a.lower():
                print(f"- {p.title}: {p.content}")
                found = True
        if not found:
            print("No posts found by that author.")

    def delete_post(self, title):
        for p in self.post_list:
            if p.title.lower() == title.lower():
                self.post_list.remove(p)
                print(f" Post '{title}' deleted successfully.")
                return
        print("No post found with that title.")

    def edit_post(self, title):
        for p in self.post_list:
            if p.title.lower() == title.lower():
                new_content = input("Enter new content: ")
                p.content = new_content
                print(f"Post '{title}' updated successfully.")
                return
        print(" Post not found.")

    def display_latest_posts(self):
        if not self.post_list:
            print(" No posts yet.")
        else:
            print("\n Latest Posts:")
            for p in self.post_list[-3:]:  # Oxirgi 3 ta post
                print(f"- {p.title} by {p.author}")


def main():
    blog = Blog()

    while True:
        print("\n=== Simple Blog System ===")
        print("1.  Add Post")
        print("2.  See All Posts")
        print("3.  See Posts by Author")
        print("4.  Delete Post by Title")
        print("5.  Edit Post by Title")
        print("6.  Display Latest Posts")
        print("7.  Exit")

        choice = input("\nEnter your choice (17): ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == '2':
            blog.see_all_posts()

        elif choice == '3':
            blog.display_posts_by_author()

        elif choice == '4':
            title = input("Enter post title to delete: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Enter post title to edit: ")
            blog.edit_post(title)

        elif choice == '6':
            blog.display_latest_posts()

        elif choice == '7':
            print(" Exiting the Blog System. Goodbye!")
            break

        else:
            print(" Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()

class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {amount} som depozit qilindi. Yangi balans: {self.balance}")
        else:
            print("Notogri miqdor kiritildi.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f" {amount} som yechildi. Qolgan balans: {self.balance}")
        else:
            print("Mablag yetarli emas yoki notogri miqdor kiritildi.")

    def display(self):
        print(f"\n Account raqami: {self.acc_number}\n Egasi: {self.holder_name}\n Balans: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Hisob raqami {account.acc_number} muvaffaqiyatli ochildi!")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"{acc.holder_name} balansida: {acc.balance} som bor.")
        else:
            print("Bunday hisob topilmadi.")

    def deposit_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Hisob topilmadi.")

    def withdraw_money(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Hisob topilmadi.")

    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f" {sender.holder_name} dan {receiver.holder_name} ga {amount} som otkazildi.")
            else:
                print("Jonatuvchining balansida mablag yetarli emas.")
        else:
            print("Hisoblardan biri topilmadi.")


def main():
    bank = Bank()

    while True:
        print("\n=== Simple Banking System ===")
        print("1.  Yangi hisob ochish")
        print("2.  Balansni tekshirish")
        print("3. Depozit qilish")
        print("4.  Pul yechish")
        print("5.  Pul otkazish (transfer)")
        print("6.  Hisob malumotlarini korish")
        print("7. Chiqish")

        choice = input("Tanlang (1-7): ")

        if choice == '1':
            acc_number = input("Hisob raqamini kiriting: ")
            holder_name = input("Hisob egasining ismini kiriting: ")
            account = Account(acc_number, holder_name)
            bank.add_account(account)

        elif choice == '2':
            acc_number = input("Hisob raqamini kiriting: ")
            bank.check_balance(acc_number)

        elif choice == '3':
            acc_number = input("Hisob raqamini kiriting: ")
            amount = float(input("Summani kiriting: "))
            bank.deposit_money(acc_number, amount)

        elif choice == '4':
            acc_number = input("Hisob raqamini kiriting: ")
            amount = float(input("Yechiladigan summani kiriting: "))
            bank.withdraw_money(acc_number, amount)

        elif choice == '5':
            from_acc = input("Jonatuvchi hisob raqami: ")
            to_acc = input("Qabul qiluvchi hisob raqami: ")
            amount = float(input("Otkaziladigan summani kiriting: "))
            bank.transfer_money(from_acc, to_acc, amount)

        elif choice == '6':
            acc_number = input("Hisob raqamini kiriting: ")
            acc = bank.find_account(acc_number)
            if acc:
                acc.display()
            else:
                print("Bunday hisob topilmadi.")

        elif choice == '7':
            print("Dasturdan chiqildi. Rahmat!")
            break

        else:
            print(" Notogri tanlov. Qayta urinib koring.")

 
main()
