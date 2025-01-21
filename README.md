# Gas Utility Customer Service Application

Welcome to the **Gas Utility Customer Service System🔥 **! This web-based application is designed to efficiently handle customer service requests for a gas utility company. 
The system facilitates online service request submission, tracking, and seamless communication between customers and the admin.

---

## **Features**

### Customer Features
1. **Submit Requests**: Customers can submit service requests by filling out a detailed form.
2. **Upload Files**: Optionally upload a file related to the issue (e.g., images, documents).
3. **Receive Tracking ID**: Automatically receive a tracking ID via email after submission.
4. **Track Requests**: Check the status of their requests using the tracking ID on the home page.
5. **Receive Updates**: Get email notifications whenever the status of their request changes.

### Admin Features
1. **View Requests**: Access a list of all service requests, including customer details.
2. **Update Status**: Change the status of requests (e.g., Pending, In Progress, Resolved).
3. **View Uploaded Files**: Download and view files uploaded by customers.
4. **Set Tentative Dates**: Provide estimated resolution dates for issues.

---

## **Tech Stack👩🏻‍💻 **
- **Backend Framework:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Email Service:** SMTP (with Gmail or any compatible SMTP server)
- **UUID for Tracking IDs**

---

## **Screenshots**

![Screenshot 2025-01-20 144510](https://github.com/user-attachments/assets/2b2afc74-e013-4d68-a62d-ac7bf870edf5)
![Screenshot 2025-01-20 144612](https://github.com/user-attachments/assets/6289d0d2-e966-49e2-9f04-a0472062e026)
![Screenshot 2025-01-20 144645](https://github.com/user-attachments/assets/b31296fd-a099-480b-8bd6-4cd56d9a41f8)
![Screenshot 2025-01-20 144725](https://github.com/user-attachments/assets/7c319396-bcb9-4f65-bb3e-bf3abf39304c)
![photo](https://github.com/user-attachments/assets/efc5ce21-751a-4146-9ae9-dbcae0da5ab0)
![Screenshot 2025-01-20 145218](https://github.com/user-attachments/assets/80acb0fe-bbf3-4af3-8b3b-9689e78d3e9f)
![Screenshot 2025-01-20 145246](https://github.com/user-attachments/assets/d65c7653-ab9f-4f34-a0ea-9076aebd4956)
![Screenshot 2025-01-20 145359](https://github.com/user-attachments/assets/12171ae5-2464-4289-97f3-982287105582)
![Screenshot 2025-01-20 145439](https://github.com/user-attachments/assets/1d42e597-4286-48b5-b00c-d996b2107b89)



---

## **How to Interact with the System**

### **1. Customer Interaction**
1. Visit the home page and navigate to the "Submit Request" section.
2. Fill out the issue form with details like:
   - Your Name
   - Email Address
   - Contact Number
   - Issue Description
3. Click **Submit** to send your request. You will:
   - See a "Thank You" page with a button to return to the home page.
   - Receive an email with your unique `Tracking ID`.

4. Use the **Tracking Section** on the home page to track your request. Enter your `Tracking ID` and click **Track** to view:
   - Status of your request.
   - Resolution progress.
   - Tentative resolution date (if provided).

---

### **2. Admin Interaction**
1. Log in to the admin interface: `/admin`.
2. View and manage customer requests, including:
   - Updating the status (Pending, In Progress, Resolved).
   - Adding a tentative resolution date.
3. Changes are automatically communicated to the customer via email.

---

## Deployment Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd GasUtility
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application in your browser at `http://127.0.0.1:8000/`.

---

ADMIN SECTION--
username - Tushar
Password - Kedar0510

You can add yourself also 

---


THANK YOU...🙌😁
