# StudentDetailsApp

This repo have Api genetared using Django REST Framework.

The aim of this project is to allow user(teacher) of the school to make, update, delete and view the student Tshirt details record.

This project have two modules _User(teacher)_ and _Student Tshirt Details_ module.

**_User Module_**
- Have the permission to create to student Tshirt details entry.
- View the student record.
- View, delete and update the individual student enrty.

**_Student Tshirt Details_**
- Have the entries of student Tshirt details record.
- Have foreign key relationship with user(_teacher_).

**Permissions**
- Only authnicated user have permission to perform action on student Tshirt details records (_the user who create the record_).
- Only Admin have the permission to view the Users(_teacher's_) list and student records created by the individual User by provinding the user id.
