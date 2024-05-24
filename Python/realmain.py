import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QTableWidgetItem, QLabel
from PyQt6.QtCore import QDate
from PyQt6 import uic
import mysql.connector
from mysql.connector import errorcode

class UserLogIn(QDialog):
    def __init__(self):
        super(UserLogIn, self).__init__()
        uic.loadUi('TestFinals/userUI.ui', self) 

        self.enterButton.clicked.connect(self.checker)
        self.registerButton.clicked.connect(self.go_to_register)


    def checker(self):
        username = self.lineName.text()  
        password = self.linePass.text()  

        if username == '' and password == '':
            QMessageBox.about(self, 'Error', 'Please enter the required information!')
        elif self.validate(username, password):
            user_id = self.get_user_id(username, password)
            if user_id is not None:
                self.openMainUser(user_id)
            else:
                QMessageBox.about(self, 'Error', 'Failed to retrieve user ID!')
        else:
            QMessageBox.about(self, 'Error', 'Incorrect Username or Password!')

    def validate(self, username, password):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT * FROM tblUserLoginData WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            row = cursor.fetchone()
            cursor.close()
            con.close()

            return row is not None  
        
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False
        
    def openMainUser(self,user_id):
        self.userDashboard = userDashboard(user_id)  
        self.userDashboard.show()  
        self.close()

    def get_user_id(self, username, password):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT id FROM tblUserLoginData WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0]
            else:
                return None
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None
        
    def go_to_register(self):
        self.register = registerPersonalInformation()  
        self.register.show()  
        self.close()
        
class registerPersonalInformation(QDialog):
    def __init__(self, fname='', mname='', lname='',email='', home=''):
        super(registerPersonalInformation, self).__init__()
        uic.loadUi('TestFinals/registerPersonalInfromationUI.ui', self)  

        self.populate_nationality_combobox()

        self.lineFname.setText(fname)
        self.lineMname.setText(mname)
        self.lineLname.setText(lname)

        self.dateEdit.setDate(QDate.currentDate())
        self.lineEmail.setText(email)
        self.textHome.setPlainText(home)

        self.nextButton.clicked.connect(self.nextInfo)
        self.backButton.clicked.connect(self.goback)


    def populate_nationality_combobox(self):
        # List of nationalities (this is a sample list, you can use a more comprehensive one)
        nationalities = [
            "","Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Antiguans",
            "Argentinean", "Armenian", "Australian", "Austrian", "Azerbaijani", "Bahamian",
            "Bahraini", "Bangladeshi", "Barbadian", "Barbudans", "Batswana", "Belarusian",
            "Belgian", "Belizean", "Beninese", "Bhutanese", "Bolivian", "Bosnian", "Brazilian",
            "British", "Bruneian", "Bulgarian", "Burkinabe", "Burmese", "Burundian", "Cambodian",
            "Cameroonian", "Canadian", "Cape Verdean", "Central African", "Chadian", "Chilean",
            "Chinese", "Colombian", "Comoran", "Congolese", "Costa Rican", "Croatian", "Cuban",
            "Cypriot", "Czech", "Danish", "Djibouti", "Dominican", "Dutch", "East Timorese",
            "Ecuadorean", "Egyptian", "Emirian", "Equatorial Guinean", "Eritrean", "Estonian",
            "Ethiopian", "Fijian", "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian",
            "German", "Ghanaian", "Greek", "Grenadian", "Guatemalan", "Guinea-Bissauan", "Guinean",
            "Guyanese", "Haitian", "Herzegovinian", "Honduran", "Hungarian", "Icelander", "Indian",
            "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican",
            "Japanese", "Jordanian", "Kazakhstani", "Kenyan", "Kittian and Nevisian", "Kuwaiti",
            "Kyrgyz", "Laotian", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtensteiner",
            "Lithuanian", "Luxembourger", "Macedonian", "Malagasy", "Malawian", "Malaysian",
            "Maldivan", "Malian", "Maltese", "Marshallese", "Mauritanian", "Mauritian", "Mexican",
            "Micronesian", "Moldovan", "Monacan", "Mongolian", "Moroccan", "Mosotho", "Motswana",
            "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerien",
            "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Panamanian",
            "Papua New Guinean", "Paraguayan", "Peruvian", "Polish", "Portuguese", "Qatari", "Romanian",
            "Russian", "Rwandan", "Saint Lucian", "Salvadoran", "Samoan", "San Marinese", "Sao Tomean",
            "Saudi", "Scottish", "Senegalese", "Serbian", "Seychellois", "Sierra Leonean", "Singaporean",
            "Slovakian", "Slovenian", "Solomon Islander", "Somali", "South African", "South Korean",
            "Spanish", "Sri Lankan", "Sudanese", "Surinamer", "Swazi", "Swedish", "Swiss", "Syrian",
            "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian/Tobagonian",
            "Tunisian", "Turkish", "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbekistani",
            "Venezuelan", "Vietnamese", "Welsh", "Yemenite", "Zambian", "Zimbabwean"
        ]

        self.nationalityComboBox.addItems(nationalities)

    def nextInfo(self):
        firstname = self.lineFname.text()
        middlename = self.lineMname.text()
        lastname = self.lineLname.text()
        birthdate = self.dateEdit.date().toString("dd-MM-yyyy")
        nationality = self.nationalityComboBox.currentText()
        emailaddress = self.lineEmail.text()
        homeaddress = self.textHome.toPlainText()

        if not firstname or not middlename or not lastname or not birthdate or not nationality or not emailaddress or not homeaddress:
            QMessageBox.warning(self, 'Error', 'Please fill in all required fields!')
            return
        
        self.registerUsernamePassword = registerUsernamePassword(firstname, middlename, lastname, birthdate, nationality, emailaddress, homeaddress)
        self.registerUsernamePassword.show()
        self.close()

    def goback(self):
        self.backs = UserLogIn()
        self.backs.show()
        self.close()        

class registerUsernamePassword(QDialog):
    def __init__(self, Fname, Mname, Lname, Bdate, nationality, email, home, username=''):
        super(registerUsernamePassword, self).__init__()
        uic.loadUi('TestFinals/registerLoginUI.ui', self)  

        self.firstname = Fname
        self.middlename = Mname
        self.lastname = Lname
        self.birthdate = Bdate
        self.nationality = nationality
        self.email = email
        self.homeaddress = home

        self.lineUname.setText(username)

        self.backButton.clicked.connect(self.go_back)
        self.nextButton.clicked.connect(self.registerLogIn)

    def registerLogIn(self):
        username = self.lineUname.text()
        password = self.linePass.text()
        confirm_password = self.lineCpass.text()

        if not username or not password or not confirm_password:
            QMessageBox.warning(self, 'Error', 'Please fill in all required fields!')
            return

        if password != confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match!')
            return

        self.reviewInfo = reviewInformation(
            self.firstname, self.middlename, self.lastname, self.birthdate, self.nationality,self.email, self.homeaddress, username, password
        )
        self.reviewInfo.show()
        self.close()

    def go_back(self):
        self.registerPersonalInfo = registerPersonalInformation(
            fname = self.firstname,
            mname = self.middlename,
            lname = self.lastname,
            email = self.email,
            home = self.homeaddress
        )
        self.registerPersonalInfo.show()
        self.close()

class reviewInformation(QDialog):
    def __init__(self, Fname, Mname, Lname, Bdate, Nationality, Email, Home, usern, Password):
        super(reviewInformation, self).__init__()
        uic.loadUi('TestFinals/reviewInformationUI.ui', self)  

        self.firstname = Fname
        self.middlename = Mname
        self.lastname = Lname
        self.birthdate = Bdate
        self.nationality = Nationality
        self.email = Email
        self.homeaddress = Home

        self.username = usern
        self.password = Password

        self.labelFname.setText(self.firstname)
        self.labelMname.setText(self.middlename)
        self.labelLname.setText(self.lastname)
        self.labelBdate.setText(self.birthdate)
        self.labelNationality.setText(self.nationality)
        self.labelEmail.setText(self.email)
        self.labelHome.setText(self.homeaddress)

        self.nextButton.clicked.connect(self.confirm)
        self.cancelButton.clicked.connect(self.go_back)

    def openMainUser(self,user_id):
        self.userDashboard = userDashboard(user_id)  
        self.userDashboard.show()  
        self.close()

    def confirm(self):
        self.userID = self.generate_user_id()

        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()

            cursor.execute(
                "INSERT INTO tblUserLoginData (id, username, password) VALUES (%s, %s, %s)",
                (self.userID, self.username, self.password)
            )

            cursor.execute(
                "INSERT INTO tblUserbalance (id, balance) VALUES (%s, %s)",
                (self.userID, 0.0)
            )

            cursor.execute(
                "INSERT INTO tbluserpersonalinformation (id, firstname, middlename, lastname, birthdate, nationality, emailaddress, homeaddress) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.userID, self.firstname, self.middlename, self.lastname, self.birthdate, self.nationality, self.email, self.homeaddress)
            )

            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, 'Success', 'User registered successfully!')
            self.openMainUser(self.userID)

        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Error', f"Failed to register user: {err}")

    def go_back(self):
        self.registerUsernamePassword = registerUsernamePassword(
            self.firstname,
            self.middlename,
            self.lastname,
            self.birthdate,
            self.nationality,
            self.email,
            self.homeaddress,
            self.username
        )
        self.registerUsernamePassword.show()
        self.close()

    def generate_user_id(self):
        current_year = QDate.currentDate().year() % 100  # Get the last two digits of the current year
        prefix = f"U{current_year:02d}-"

        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()

            # Fetch the last used user number
            cursor.execute("SELECT last_user_number FROM tblUserIDTracker WHERE id = 1")
            row = cursor.fetchone()

            if row:
                last_number = row[0]
                new_number = last_number + 1

                # Update the last used user number
                cursor.execute("UPDATE tblUserIDTracker SET last_user_number = %s WHERE id = 1", (new_number,))
                con.commit()

                new_id = f"{prefix}{new_number:04d}"
            else:
                new_id = f"{prefix}0000"

            cursor.close()
            con.close()
            return new_id

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return f"{prefix}0000"

class userDashboard(QDialog):
    def __init__(self, user_id):
        super(userDashboard, self).__init__()
        uic.loadUi('TestFinals/userMainUI.ui', self) 

        self.id = user_id

        self.userfirstname.setText(str(self.get_info_from_id('firstname', 'tbluserpersonalinformation')))
        self.usersbalance.setText(str(f"₱{self.get_info_from_id('balance','tbluserbalance'):.2f}"))
        

        self.accountButton.clicked.connect(self.open_settings)
        self.depositButton.clicked.connect(self.make_deposit)
        self.transferButton.clicked.connect(self.make_transfer)
        self.withdrawButton.clicked.connect(self.make_withdrawal)
        self.historyButton.clicked.connect(self.show_history)

        self.show_recent()

        self.type1 = QLabel()
        self.type2 = QLabel()
        self.type3 = QLabel()
        self.amount1 = QLabel()
        self.amount2 = QLabel()
        self.amount3 = QLabel()


    def recent_history(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT transaction_type, amount FROM transaction_history WHERE id = %s order by timestamp DESC limit 3;"
            cursor.execute(query, (self.id,))
            records = cursor.fetchall()
            con.close()

            return records
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None
        
    def set_label_text_and_style(self, type_label, amount_label, record_type, record_amount):
        type_label.setText(record_type)
        amount_label.setText(f"₱{record_amount:.2f}")
        
        if record_type.lower() == "withdraw":
            amount_label.setStyleSheet("color: red; background-color: transparent;")
        elif record_type.lower() == "deposit" or record_type.lower() == "receive":
            amount_label.setStyleSheet("color: #46DB00; background-color: transparent;")
        elif record_type.lower() == "":
            amount_label.setStyleSheet("background-color: transparent;")

        if type_label == "":
            amount_label.setStyleSheet("background-color: transparent;")

    def clear_label_text_and_style(self, type_label, amount_label):
        type_label.setText("")
        amount_label.setText("")
        amount_label.setStyleSheet("background-color: transparent;")

    def show_recent(self):
        records = self.recent_history()

        labels = [(self.type1, self.amount1), (self.type2, self.amount2), (self.type3, self.amount3)]
        for i, (type_label, amount_label) in enumerate(labels):
            if i < len(records):
                self.set_label_text_and_style(type_label, amount_label, records[i][0], records[i][1])
            else:
                self.clear_label_text_and_style(type_label, amount_label)

    def get_info_from_id(self, field, database):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM {database} WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0] 
            else:
                return None
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def open_settings(self):
        self.settingsAccount_window = settingsAccount(self.id)
        self.settingsAccount_window.show()
        self.close()

    def make_deposit(self):
        self.deposit_window = deposit(self.id)
        self.deposit_window.show()
        self.close()

    def make_transfer(self):
        self.transfer_window = transfer(self.id)
        self.transfer_window.show()
        self.close()

    def make_withdrawal(self):
        self.withdraw_window = withdraw(self.id)
        self.withdraw_window.show()
        self.close()

    def show_history(self):
        self.history_window = history(self.id)
        self.history_window.show()
        self.close()

class settingsAccount(QDialog):
    def __init__(self, user_id):
        super(settingsAccount, self).__init__()
        uic.loadUi('TestFinals/accountUI.ui', self)  

        self.id = user_id

        self.backButton.clicked.connect(self.back_to_userdashboard)
        self.updateButton.clicked.connect(self.go_to_update)
        self.deleteButton.clicked.connect(self.delete_account)
        self.logoutButton.clicked.connect(self.logout)


        self.fullname_2.setText(self.get_info_from_id("CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname", ))
        self.userid_2.setText(str(self.id))
        self.birthdate.setText(self.get_info_from_id('birthdate'))
        self.nationality.setText(self.get_info_from_id('nationality'))
        self.email.setText(self.get_info_from_id('emailaddress'))
        self.homeaddress.setText(self.get_info_from_id('homeaddress'))

    def get_info_from_id(self, field):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM tbluserpersonalinformation WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0] 
            else:
                return None
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def back_to_main(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close()

    def go_to_update(self):
        self.update = updateInformation(self.id)
        self.update.show()
        self.close()

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close()

    def delete_account(self):
        self.confirm_delete_dialog = confirmDelete(self.id)
        self.confirm_delete_dialog.show()
        self.close()

    def logout(self):
        self.backs = UserLogIn()
        self.backs.show()
        self.close()

class confirmDelete(QDialog):
    def __init__(self, user_id):
        super(confirmDelete, self).__init__()
        uic.loadUi('TestFinals/confirmdeleteUI.ui', self)  

        self.id = user_id

        self.confirmButton.clicked.connect(self.confirm_deletion)
        self.cancelButton.clicked.connect(self.cancel_deletion)

    def confirm_deletion(self):
        password = self.passwordInput.text()
        if self.verify_password(password):
            if self.check_balance():
                self.delete_account()
            else:
                QMessageBox.warning(self, "Error", "You cannot delete your account because you still have a balance.")
        else:
            QMessageBox.warning(self, "Error", "Incorrect password.")

    def verify_password(self, password):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT password FROM tbluserlogindata WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row and row[0] == password:  
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False

    def check_balance(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT balance FROM tbluserbalance WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row and row[0] == 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False

    def delete_account(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
     
            delete_queries = [
                "DELETE FROM tbluserpersonalinformation WHERE id = %s",
                "DELETE FROM tbluserbalance WHERE id = %s",
                "DELETE FROM tbluserlogindata WHERE id = %s",
                "DELETE FROM transaction_history WHERE id = %s"
            ]
            for query in delete_queries:
                cursor.execute(query, (self.id,))
            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, "Success", "Your account has been deleted.")
            self.logout()
            self.close()

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            QMessageBox.critical(self, "Database Error", "An error occurred while deleting your account.")

    def cancel_deletion(self):
        self.backs = settingsAccount(self.id)
        self.backs.show()
        self.close()


    def logout(self):
        self.backs = UserLogIn()
        self.backs.show()
        self.close()


class updateInformation(QDialog):
    def __init__(self, user_id):
        super(updateInformation, self).__init__()
        uic.loadUi('TestFinals/updateUI.ui', self) 

        self.id = user_id

        self.cancelButton.clicked.connect(self.back_to_userdashboard)
        self.saveButton.clicked.connect(self.save_changes)

        self.linefname.setText(str(self.get_info_from_id('firstname')))
        self.linemname.setText(str(self.get_info_from_id('middlename')))
        self.linelname.setText(str(self.get_info_from_id('lastname')))
        self.linebdate.setText(str(self.get_info_from_id('birthdate')))
        self.linenationality.setText(str(self.get_info_from_id('nationality')))
        self.lineemail.setText(str(self.get_info_from_id('emailaddress')))
        self.lineaddress.setText(str(self.get_info_from_id('homeaddress')))


    def get_info_from_id(self, field):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM tbluserpersonalinformation WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0] 
            else:
                return None
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None
        
    def save_changes(self):

        firstname = self.linefname.text()
        middlename = self.linemname.text()
        lastname = self.linelname.text()
        birthdate = self.linebdate.text()
        nationality = self.linenationality.text()
        emailaddress = self.lineemail.text()
        homeaddress = self.lineaddress.text()

        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = """
                UPDATE tbluserpersonalinformation
                SET firstname = %s, middlename = %s, lastname = %s, birthdate = %s, nationality = %s, emailaddress = %s, homeaddress = %s
                WHERE id = %s
            """
            cursor.execute(query, (firstname, middlename, lastname, birthdate, nationality, emailaddress, homeaddress, self.id))
            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, 'Success', 'User information updated successfully.')
            self.back_to_userdashboard()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            QMessageBox.critical(self, 'Error', f"An error occurred: {err}")

    def back_to_userdashboard(self):
        reply = QMessageBox.question(self, 'Confirm Discard', 'Are you sure you want to discard the changes?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.backs = userDashboard(self.id)
            self.backs.show()
            self.close() 


class deposit(QDialog):
    def __init__(self, user_id):
        super(deposit, self).__init__()
        uic.loadUi('TestFinals/depositUI.ui', self)  

        self.id = user_id

        self.backButton.clicked.connect(self.back_to_userdashboard)
        self.nextButton.clicked.connect(self.validate_deposit)

        self.button15.clicked.connect(lambda: self.set_amount(15))
        self.button50.clicked.connect(lambda: self.set_amount(50))
        self.button75.clicked.connect(lambda: self.set_amount(75))

        self.button100.clicked.connect(lambda: self.set_amount(100))
        self.button150.clicked.connect(lambda: self.set_amount(150))
        self.button200.clicked.connect(lambda: self.set_amount(200))

        self.button300.clicked.connect(lambda: self.set_amount(300))
        self.button500.clicked.connect(lambda: self.set_amount(500))
        self.button1000.clicked.connect(lambda: self.set_amount(1000))

    def set_amount(self, amount):
        self.lineAmount.setText(str(amount))

    def validate_deposit(self):

        sender = self.fromwho.currentText() 

        try:
            amount = float(self.lineAmount.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
            return

        if amount <= 0:
            QMessageBox.warning(self, "Input Error", "Please enter an amount greater than zero.")
            return

        self.confirmation_dialog = DepositConfirmation(self.id, amount,sender)
        self.confirmation_dialog.show()
        self.close()

    def get_balance_from_id(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT balance FROM tbluserbalance WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0]
            else:
                return None

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close()


class DepositConfirmation(QDialog):
    def __init__(self, user_id, amount, sender):
        super(DepositConfirmation, self).__init__()
        uic.loadUi('TestFinals/depositconfirmationUI.ui', self)  

        self.user_id = user_id
        self.amount = amount
        self.senders = sender

        self.confirmButton.clicked.connect(self.complete_deposit)
        self.cancelButton.clicked.connect(self.back_to_deposit)

        self.receiverName.setText(str(self.get_info_from_id("CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname", "tbluserpersonalinformation", self.user_id)))
        self.receiverID.setText(str(user_id))
        self.amounttosend.setText(f"₱{amount:.2f}")
        self.amount1.setText(f"₱{amount:.2f}")
        self.depositType.setText(self.senders) 

        self.userbalance.setText(str(f"₱{self.get_info_from_id('balance', 'tbluserbalance', self.user_id):.2f}"))

    def get_info_from_id(self, field, database, id):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM {database} WHERE id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0]
            else:
                return None

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def complete_deposit(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()

            # Add amount to user's account
            add_query = "UPDATE tbluserbalance SET balance = balance + %s WHERE id = %s"
            cursor.execute(add_query, (float(self.amount), self.user_id,))

            # Insert transaction for deposit
            insert_deposit_query = "INSERT INTO transaction_history (id, transaction_type, amount, related_user_id) VALUES (%s, 'deposit', %s, %s)"
            cursor.execute(insert_deposit_query, (self.user_id, float(self.amount), self.senders,))

            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, "Success", "Deposit completed successfully.")
            self.back_to_userdashboard()

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            QMessageBox.critical(self, "Database Error", "An error occurred during the deposit.")

    def back_to_deposit(self):
        self.deposit_dialog = deposit(self.user_id)
        self.deposit_dialog.show()
        self.close()

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.user_id)
        self.backs.show()
        self.close()

class transfer(QDialog):
    def __init__(self, user_id):
        super(transfer, self).__init__()
        uic.loadUi('TestFinals/transferUI.ui', self)  

        self.id = user_id

        self.userbalance.setText(str(f"₱{self.get_balance_from_id():.2f}"))

        self.backButton.clicked.connect(self.back_to_userdashboard)
        self.nextButton.clicked.connect(self.validate_transfer)

        self.button15_2.clicked.connect(lambda: self.set_amount(15))
        self.button50_2.clicked.connect(lambda: self.set_amount(50))
        self.button75_2.clicked.connect(lambda: self.set_amount(75))

        self.button100_2.clicked.connect(lambda: self.set_amount(100))
        self.button150_2.clicked.connect(lambda: self.set_amount(150))
        self.button200_2.clicked.connect(lambda: self.set_amount(200))

        self.button300_2.clicked.connect(lambda: self.set_amount(300))
        self.button500_2.clicked.connect(lambda: self.set_amount(500))
        self.button1000_2.clicked.connect(lambda: self.set_amount(1000))

    def set_amount(self, amount):
        self.lineAmount.setText(str(amount))

    def validate_transfer(self):
        recipient_id = str(self.linerecepientID.text())
        try:
            amount = float(self.lineAmount.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
            return

        if not recipient_id or not amount:
            QMessageBox.warning(self, "Input Error", "Please enter both recipient ID and amount.")
            return

        user_balance = self.get_balance_from_id()
        if user_balance is None:
            QMessageBox.critical(self, "Error", "Could not retrieve your balance.")
            return

        if amount > user_balance:
            QMessageBox.warning(self, "Insufficient Funds", "You do not have enough balance to complete this transfer.")
            return

        if not self.recipient_exists(recipient_id):
            QMessageBox.warning(self, "Input Error", "Recipient ID does not exist.")
            return

        self.confirmation_dialog = TransferConfirmation(self.id, recipient_id, amount)
        self.confirmation_dialog.show()
        self.close()

    def recipient_exists(self, recipient_id):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT 1 FROM tbluserbalance WHERE id = %s"
            cursor.execute(query, (recipient_id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            return row is not None

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return False

    def get_balance_from_id(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT balance FROM tbluserbalance WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0] 
            else:
                return None
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close() 

class TransferConfirmation(QDialog):
    def __init__(self, user_id, recipient_id, amount):
        super(TransferConfirmation, self).__init__()
        uic.loadUi('TestFinals/confirmationUI.ui', self)

        self.user_id = user_id
        self.recipient_id = recipient_id
        self.amount = amount

        self.confirmButton_2.clicked.connect(self.complete_transfer)
        self.cancelButton_2.clicked.connect(self.back_to_transfer)

    
        self.senderName.setText(str(self.get_info_from_id("CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname", "tbluserpersonalinformation",self.user_id)))
        self.receiverName.setText(str(self.get_info_from_id("CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname", "tbluserpersonalinformation",self.recipient_id)))
        self.receiverID.setText(str(recipient_id))
        self.amounttosend_2.setText(f"₱{amount:.2f}")
        self.amount1.setText(f"₱{amount:.2f}")

        self.userbalance.setText(str(f"₱{self.get_info_from_id('balance', 'tbluserbalance', self.user_id):.2f}"))

    def get_info_from_id(self, field, database, id):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM {database} WHERE id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0] 
            else:
                return None
            
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def complete_transfer(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()

            # Deduct amount from sender's account
            deduct_query = "UPDATE tbluserbalance SET balance = balance - %s WHERE id = %s"
            cursor.execute(deduct_query, (float(self.amount), self.user_id,))

            # Add amount to recipient's account
            add_query = "UPDATE tbluserbalance SET balance = balance + %s WHERE id = %s"
            cursor.execute(add_query, (float(self.amount), self.recipient_id,))

            # Insert transaction for sender
            insert_sender_query = "INSERT INTO transaction_history (id, transaction_type, amount, related_user_id) VALUES (%s, 'transfer', %s, %s)"
            cursor.execute(insert_sender_query, (self.user_id, float(self.amount), self.recipient_id,))

            # Insert transaction for recipient
            insert_recipient_query = "INSERT INTO transaction_history (id, transaction_type, amount, related_user_id) VALUES (%s, 'receive', %s, %s)"
            cursor.execute(insert_recipient_query, (self.recipient_id, float(self.amount), self.user_id,))

            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, "Success", "Transfer completed successfully.")
            self.back_to_userdashboard()

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            QMessageBox.critical(self, "Database Error", "An error occurred during the transfer.")

    def back_to_transfer(self):
        self.transfer_dialog = transfer(self.user_id)
        self.transfer_dialog.show()
        self.close()

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.user_id)
        self.backs.show()
        self.close()

class withdraw(QDialog):
    def __init__(self, user_id):
        super(withdraw, self).__init__()
        uic.loadUi('TestFinals/withdrawUI.ui', self)  

        self.id = user_id

        self.userbalance.setText(str(f"₱{self.get_balance_from_id():.2f}"))

        self.backButton_2.clicked.connect(self.back_to_userdashboard)
        self.nextButton_3.clicked.connect(self.validate_withdraw)

        self.button15_3.clicked.connect(lambda: self.set_amount(15))
        self.button50_3.clicked.connect(lambda: self.set_amount(50))
        self.button75_3.clicked.connect(lambda: self.set_amount(75))

        self.button100_3.clicked.connect(lambda: self.set_amount(100))
        self.button150_3.clicked.connect(lambda: self.set_amount(150))
        self.button200_3.clicked.connect(lambda: self.set_amount(200))

        self.button300_3.clicked.connect(lambda: self.set_amount(300))
        self.button500_3.clicked.connect(lambda: self.set_amount(500))
        self.button1000_3.clicked.connect(lambda: self.set_amount(1000))

    def set_amount(self, amount):
        self.lineAmount_3.setText(str(amount))

    def validate_withdraw(self):

        user_balance = self.get_balance_from_id()
        recepient = self.withdrawType.currentText() 

        try:
            amount = float(self.lineAmount_3.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid amount.")
            return

        if amount > user_balance:
            QMessageBox.warning(self, "Input Error", "Insufficent Funds")
            return
        
        self.confirmation_dialog = withdrawConfirmation(self.id, amount,recepient)
        self.confirmation_dialog.show()
        self.close()

    def get_balance_from_id(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT balance FROM tbluserbalance WHERE id = %s"
            cursor.execute(query, (self.id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0]
            else:
                return None

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close()

class withdrawConfirmation(QDialog):
    def __init__(self, user_id, amount, recepient):
        super(withdrawConfirmation, self).__init__()
        uic.loadUi('TestFinals/withdrawconfirmationUI.ui', self)  # Load the main UI

        self.user_id = user_id
        self.amount = amount
        self.recepient = recepient

        self.confirmButton.clicked.connect(self.complete_withdraw)
        self.cancelButton.clicked.connect(self.back_to_withdraw)

        self.sendername.setText(str(self.get_info_from_id("CONCAT(firstname, ' ', COALESCE(lastname, '')) AS fullname", "tbluserpersonalinformation", self.user_id)))
 
        self.amounttosend.setText(f"₱{amount:.2f}")
        self.withdrawType.setText(self.recepient)  

        self.userbalance.setText(str(f"₱{self.get_info_from_id('balance', 'tbluserbalance', self.user_id):.2f}"))
        self.amount2.setText(f"₱{amount:.2f}")

    def get_info_from_id(self, field, database, id):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = f"SELECT {field} FROM {database} WHERE id = %s"
            cursor.execute(query, (id,))
            row = cursor.fetchone()
            cursor.close()
            con.close()
            if row:
                return row[0]
            else:
                return None

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            return None

    def complete_withdraw(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()

            # Add amount to user's account
            minus_query = "UPDATE tbluserbalance SET balance = balance - %s WHERE id = %s"
            cursor.execute(minus_query, (float(self.amount), self.user_id,))

            # Insert transaction for deposit
            insert_deposit_query = "INSERT INTO transaction_history (id, transaction_type, amount, related_user_id) VALUES (%s, 'withdraw', %s, %s)"
            cursor.execute(insert_deposit_query, (self.user_id, float(self.amount), self.recepient,))

            con.commit()
            cursor.close()
            con.close()

            QMessageBox.information(self, "Success", "Withdraw completed successfully.")
            self.back_to_userdashboard()

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            QMessageBox.critical(self, "Database Error", "An error occurred during the withdraw.")

    def back_to_withdraw(self):
        self.deposit_dialog = withdraw(self.user_id)
        self.deposit_dialog.show()
        self.close()

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.user_id)
        self.backs.show()
        self.close()


class history(QDialog):
    def __init__(self,user_id):
        super(history, self).__init__()
        uic.loadUi('TestFinals/historyUI.ui', self)   

        self.id = user_id
        self.load_transactions()

        self.backButton.clicked.connect(self.back_to_userdashboard)


    def load_transactions(self):
        try:
            con = mysql.connector.connect(user="newuser", password="nikolas25!.", host="localhost", database="userdata")
            cursor = con.cursor()
            query = "SELECT transaction_type, amount, related_user_id, timestamp FROM transaction_history WHERE id = %s order by timestamp DESC"
            cursor.execute(query, (self.id,))
            transactions = cursor.fetchall()
            cursor.close()
            con.close()

            self.transactionTable.setRowCount(len(transactions))
            self.transactionTable.setColumnCount(4)
            self.transactionTable.setHorizontalHeaderLabels(['Transaction Type', 'Amount', 'Related User ID', 'Timestamp'])

            for row_num, transaction in enumerate(transactions):
                for col_num, data in enumerate(transaction):
                    self.transactionTable.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        except mysql.connector.Error as err:
            print("Error: {}".format(err))
            QMessageBox.critical(self, "Database Error", "An error occurred while fetching transaction history.")

    def close_history(self):
        self.close()

    def back_to_userdashboard(self):
        self.backs = userDashboard(self.id)
        self.backs.show()
        self.close()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = UserLogIn()
    widget.show()
    sys.exit(app.exec())