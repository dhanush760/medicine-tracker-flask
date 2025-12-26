💊 Medicine Tracker Web Application

The Medicine Tracker Web Application is a simple and user-friendly web-based system designed to help users manage their daily medications efficiently. The application allows users to add medicines, track available stock, and monitor daily reminder times through an intuitive interface. It is built using Flask for the backend and HTML and CSS for the frontend, making it lightweight, easy to understand, and suitable for beginners as well as academic projects.

The application is developed using Flask as the backend framework, HTML for structure, and CSS for styling. Gunicorn is used as the production server, and the application is deployed on the Render cloud platform.

The core functionality of the application focuses on medicine management. Users can add a medicine by providing its name, total stock, and a daily reminder time. Once added, the medicine appears under the “Saved Medicines” section, where all relevant information such as the medicine name, remaining stock, and reminder time is clearly displayed. The application prevents confusion by managing each medicine entry independently and providing clear visual separation between records.

A key feature of the system is reminder tracking through the user interface. Each medicine has a fixed daily reminder time. When the current system time reaches or exceeds this reminder time, the application displays a “Due Now” indicator next to the medicine. This serves as a visual reminder for the user to take the medication. Since the application is web-based, reminders are handled entirely within the UI and do not rely on mobile notifications or background services.

When a user clicks the “Taken” button for a medicine, the application updates multiple states at once. The stock count is reduced by one, and the system records that the medicine has been taken for the current day. As a result, the “Due Now” reminder disappears and is replaced with a taken status, ensuring the reminder does not reappear again on the same day. The reminder automatically resets on the next day, allowing the daily medication cycle to continue smoothly.

The application also includes a stock tracking mechanism. Each time a medicine is marked as taken, the remaining stock is updated and displayed in real time. If the stock reaches zero, a low stock warning is shown to alert the user that a refill is required. This helps users avoid missing doses due to unavailable medicines.

To maintain flexibility, the application provides a delete option for medicines. Users can remove any medicine entry using the delete button, which permanently removes it from the list. This ensures that outdated or unnecessary medicines do not clutter the interface.

From a technical perspective, the application uses Flask as the backend framework to handle routing, form submissions, and logic processing. The frontend is built using standard HTML and CSS, ensuring compatibility across all modern browsers. Gunicorn is used as the production server, and the application is deployed as a web service on Render, which automatically manages port binding and hosting.

The project follows a simple directory structure with separate folders for templates and static files. The templates folder contains the HTML file responsible for rendering the UI, while the static folder holds the CSS file used for styling. Dependencies such as Flask and Gunicorn are listed in the requirements.txt file to ensure smooth deployment.

Although functional, the application has certain limitations. All data is stored in memory, meaning medicines are reset when the server restarts. The system supports only one reminder per medicine per day and does not provide push notifications. Despite these limitations, the application effectively demonstrates core concepts of web development, state management, and UI-driven reminders.

Overall, the Medicine Tracker Web Application serves as a practical and educational project that showcases how a simple healthcare-related problem can be solved using web technologies. It is well-suited for academic submissions, portfolio demonstrations, and further enhancement into a full-featured medication management system.

In conclusion, the Medicine Tracker Web Application demonstrates a practical implementation of web development concepts applied to a real-world healthcare use case. It can be further enhanced by adding database storage, multi-dose reminders, and mobile notifications in future versions.

**
Live URL: https://medicine-tracker-flask.onrender.com
