(
echo # Use Case Diagram
echo.
echo ## Project
echo.
echo Expense Tracker Python ^(CLI v2.0^)
echo.
echo ---
echo.
echo ## Primary Actor
echo.
echo **User**
echo.
echo The user interacts with the Expense Tracker application to manage personal expenses.
echo.
echo ---
echo.
echo ## System Use Cases
echo.
echo - Add Expense
echo - View Expenses
echo - Search Expenses
echo - Edit Expense
echo - Delete Expense
echo - Monthly Summary
echo - Exit Application
echo.
echo ---
echo.
echo ## UML Diagram ^(PlantUML^)
echo.
echo ```plantuml
echo @startuml
echo.
echo left to right direction
echo.
echo actor User
echo.
echo rectangle "Expense Tracker System" {
echo.
echo   usecase "Add Expense" as UC1
echo   usecase "View Expenses" as UC2
echo   usecase "Search Expenses" as UC3
echo   usecase "Edit Expense" as UC4
echo   usecase "Delete Expense" as UC5
echo   usecase "Monthly Summary" as UC6
echo   usecase "Exit Application" as UC7
echo.
echo }
echo.
echo User --^> UC1
echo User --^> UC2
echo User --^> UC3
echo User --^> UC4
echo User --^> UC5
echo User --^> UC6
echo User --^> UC7
echo.
echo @enduml
echo ```
echo.
echo ---
echo.
echo ## Diagram Description
echo.
echo The user is the only actor in the system.
echo.
echo The user can:
echo.
echo - Add new expenses
echo - View all expenses
echo - Search existing expenses
echo - Edit expense details
echo - Delete expenses
echo - View monthly summaries
echo - Exit the application
echo.
echo All functionality is initiated by the user through the command-line interface.
) > docs\use_case_diagram.md