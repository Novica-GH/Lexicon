#********************************************************************************************
#  Novica Ivkovic                                                                           *
#  Cours: System Developer Python and AI                                                    *
#  September 24 2026 - LAB 9                                                                *
#             Today's study goal is:   OOP3                                                  *
#********************************************************************************************


#********************************************************************************************
#  LAB 9                     Part A - Polymorphism                                          *
#********************************************************************************************


# Part A.1. Create three classes: emailNotification, SMSNotification and PushNotification.
#------------------------------------------------------------------------------------------



# Part A.2. Give all three classes a method called sen(), but make each method return a different message.
#----------------------------------------------------------------
     


# Part A.3 Create one object from each class and store them in the same list.
#-----------------------------------------------------------------



# Part A.4 Loop through the list and call send() on every object.
#---------------------------------------------------------------------


# Part A.5 In a comment, explain why the loop does not need to know the exact class of each object.
#----------------------------------------------------------------------------------------------------------------

  
        





#***********************************************************************************************
#  LAB 9               Part B - Polymorphism with inheritance                                  *
#***********************************************************************************************


# Part B.1 Create a base class Document with a title attribute and a method describe().
#--------------------------------------------------------------------




# Part B.2 Create PDFDocument(Document) and TextDocument(Document).
#----------------------------------------------------------------------------------------------------------



# Part B.3 Override describe() in both subclasses so they return different descriptions.
#----------------------------------------------------------------------------------------------------------



# Part B.4 Create several PDFDocument and TextDocument objects and store them in one list.
#--------------------------------------------------------------------------------------




# Part B.5 Loop through the list and print each document's title and the result of describe().
#----------------------------------------------------------------------------------------------------



                  

    
#****************************************************************************************************
#  LAB 9                            PART C - Duck typing                                            *
#****************************************************************************************************


# C.1. Create two unrelated classes, for example Printer and Screen. Do not use inheritance between them.
#--------------------------------------------------------------------



# C.2 Give both classes a method called display_status().
#-----------------------------------------




# C.3 Create objects from both classes and store them in the same list.
#------------------------------------------------------------



# C.4 Loop through the list and call dispaly_status() on each object.
#------------------------------------------------------------------------------------------------



# C.5 In a comment, explain why this works even though the classes do not share a base class.
#--------------------------------------------------------------------------------------------




#************************************************************************************************
#  LAB 9                  PART D -  instance()                                                  *
#************************************************************************************************



# D.1  Create a base class User and a subclass AdminUser(User).
#-------------------------------------------------------------------------



# D.2 Create an AdminUser object.
#-------------------------------------------------------



# D.3 Use isinstance() to check whether the object is an AdminUser, a User and a string.
#--------------------------------------------------------



# D.4 Print all three results.
#-----------------------------------------------------------------------



# D.5 Ina comment, explain why the AdminUser object is also considered an instance of User.
#-----------------------------------------------------------------





#******************************************************************************************************
#  LAB 9                         Part E -     __str__                                                 *
#******************************************************************************************************


# E.1 Create a Product class with name and price.
#--------------------------------------------------------------



# E.2 Create one Product object and print it before defining  __str__. Observe the result. 
#---------------------------------------------------------------------------




# E.3 Add __str__ so printing to Product gives a useful human-readable description.
#-------------------------------------------



# E.4 Create at least three Product objects and print them.
#-------------------------------------------------------------------------------------------------


# E.5 Use str() on one Product object, store the result in a variable and print its type.
#------------------------------------------------------------------------------




#*******************************************************************************************************
#  LAB 9                    Part F -   __str__ with inheritance                                        *
#*******************************************************************************************************


# F.1 Create a base class Account with owner and balance.
#----------------------------------------------------------------------------------



# F.2 Add __str__ to Account.
#-----------------------------------------------------------------------------------------------------



# F.3 Create SavingsAccount(Account) with an additional interest_rate attribute. Use super() in __init__.
#----------------------------------------



# F.4  Override __str__ in SavingsAccount so its output also includes the interest rate.
#---------------------------------------------------



# F.5 Create and print both an Account and a SavingsAccount object.
#---------------------------------------------------------------------------------






#*******************************************************************************************************
#  LAB 9                        Part G -   Inheritance or composition?                                 *
#*******************************************************************************************************



# G.1 Create CPU with a model attribute.
#----------------------------------------------------------


# G.2 Create Computer with brand and a CPU object. Use composition, not inheritance.
#----------------------------------------------------------------------------------------


# G.3 Create a CPU object and pass it tio a Computer object.
#----------------------------------------------------------------------------------------------------


# G.4 Print the computer brand and CPU model through the Computer object.
#------------------------------------------------------------------------------------------------------------


# G.5 In comments, explain why "Computer HAS-A CPU" makes more sense tha "Computer IS-A CPU".
#---------------------------------------------------------------------------------------------




# G.6 For each pair below, write whether you would most likely use inheritance (IS-A) or composition 
#     (HAS_A): Car/ Engine, Manager/Employee, Course/Teacher, Phone/Device.





#*******************************************************************************************************
#  LAB 9                     Part H -   Applied challenge: Export system                               *
#*******************************************************************************************************


# H.1 Build a small export system using the concepts from today's lesson.
#-------------------------------------------------------------




# H.2 Create a base class Exporter with a method export(data).
#--------------------------------------------



# H.3 Dreate at least three subclasses, for example ConsoleExporter, TextExporter and SummaryExporter.
#----------------------------------------------------------------------------------------


# H.4 Override export(data) in every subclass so each handles the same data differently. You do not need to create real files. 
# ------------------------------------------------------------- 




# H.5 Add a useful __str__ mehtod to the exporter classes.
# ------------------------------------------------------------- 





# H.6 Create several exporter objects and store them in one list.
#-------------------------------------------------------------




# H.7 Loop through the list and eall export() on each object to demonstrate polymorphism
#--------------------------------------------



# H.8 Create one additional class that is not part of the Exporter inheritance hierarchy 
#     but stio provides an expoet(data) method. Show that it can be used by the same calling code.
#----------------------------------------------------------------------------------------


# H.9 Use isinstance() at least once to inspect a meaningful type relationship.
#----------------------------------------------------------------------------------------




# H.10 Add one example of composition to the program and explain the HAS-A relationship in a comment.
#----------------------------------------------------------------------------------------





# **********************************  END of LAB 9  ********************************************************