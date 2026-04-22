# 🛍️ QuickCart Pro - Ultimate E-Commerce Platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://vaishnavi-s-shinde.github.io/Quickcart-pro/)
[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue)](https://github.com/vaishnavi-s-shinde/Quickcart-pro)
[![Firebase](https://img.shields.io/badge/Firebase-Backend-orange)](https://firebase.google.com)

## 📌 Project Overview

QuickCart Pro is a **fully functional e-commerce web application** built with modern web technologies. It provides a seamless online shopping experience with features like product browsing, cart management, wishlist, order history, and PDF receipts.

### ✨ Key Features

- **🛒 Shopping Cart** - Add/remove products, quantity management, bulk discounts
- **❤️ Wishlist** - Save favorite products for later purchase
- **🔍 Smart Search** - Text search + Voice search support
- **📊 Filters & Sorting** - Category filter, price range, sort by price
- **🌓 Dark Mode** - Toggle between light and dark themes
- **📜 Order History** - View all past orders with receipts
- **📄 PDF Receipts** - Download order receipts as PDF
- **🎤 Voice Search** - Search products using voice commands
- **⌨️ Keyboard Shortcuts** - Fast navigation (Ctrl+K, Ctrl+C, etc.)
- **👑 Admin Panel** - Manage products, stock, and orders
- **📱 Responsive Design** - Works perfectly on all devices

## 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Bootstrap 5 |
| **Backend** | Firebase (Authentication, Firestore Database) |
| **APIs** | Web Speech API, QR Server API |
| **Libraries** | html2pdf, Font Awesome |
| **Deployment** | GitHub Pages |

## 🗄️ Database Structure (Firestore)

\`\`\`
users/
  └── {userId}/
      ├── name
      ├── email
      ├── credits
      └── wishlist[]

products/
  └── {productId}/
      ├── name
      ├── price
      ├── stock
      ├── category
      └── rating

orders/
  └── {orderId}/
      ├── userId
      ├── items[]
      ├── total
      ├── status
      └── createdAt
\`\`\`

## 🚀 Installation & Setup

### Prerequisites
- Modern web browser (Chrome/Firefox/Edge)
- Internet connection (for Firebase and APIs)

### Steps to Run Locally

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/vaishnavi-s-shinde/Quickcart-pro.git
   cd Quickcart-pro
   \`\`\`

2. **Open in browser**
   - Simply open \`index.html\` in your browser
   - Or use Live Server in VS Code

3. **Firebase Setup (Optional for local)**
   - Create a Firebase project
   - Enable Authentication and Firestore
   - Replace \`firebaseConfig\` in the code with your credentials

### 🔑 Test Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@quickcart.com | (any) |
| User | (register new) | (any) |

## 📱 Screenshots

| Home Page | Cart Sidebar |
|-----------|--------------|
| ![Home](screenshots/home.png) | ![Cart](screenshots/cart.png) |

| Checkout | Admin Panel |
|----------|-------------|
| ![Checkout](screenshots/checkout.png) | ![Admin](screenshots/admin.png) |

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl + K` | Focus Search |
| `Ctrl + C` | Open Cart |
| `Ctrl + H` | Go to Home |
| `Ctrl + W` | Go to Wishlist |
| `ESC` | Close Modals |
| `1-5` | Quick Add (first 5 products) |
| `?` | Show Shortcuts Help |

## 🎯 Features Demonstration

### User Flow
1. **Browse Products** - View all products with images, prices, and ratings
2. **Search/Filter** - Find products by name, category, or price range
3. **Add to Cart** - Add products with stock validation
4. **Wishlist** - Save products for later
5. **Checkout** - Fill shipping details and place order
6. **Receipt** - View and download PDF receipt
7. **Order History** - Track all past orders

### Admin Flow
1. **Login** with admin@quickcart.com
2. Click **Admin Panel** button (bottom-left)
3. **Manage Products** - Add, edit stock, delete products
4. **View Orders** - See all customer orders

## 🧪 Testing Results

| Test Case | Status |
|-----------|--------|
| Product Search | ✅ Working |
| Add to Cart | ✅ Working |
| Stock Validation | ✅ Working |
| Checkout Process | ✅ Working |
| PDF Generation | ✅ Working |
| Voice Search | ✅ Working |
| Dark Mode | ✅ Working |
| Mobile Responsive | ✅ Working |
| Firebase Auth | ✅ Working |

## 🚧 Future Enhancements

- [ ] Payment Gateway Integration (Razorpay/Stripe)
- [ ] Product Reviews & Ratings System
- [ ] Email Notifications for Orders
- [ ] Social Media Login (Google/Facebook)
- [ ] Analytics Dashboard for Admin
- [ ] Multiple Language Support

## 👨‍💻 Author

**Vaishnavi S. Shinde**
- GitHub: [@vaishnavi-s-shinde](https://github.com/vaishnavi-s-shinde)
- Project Link: [QuickCart Pro](https://vaishnavi-s-shinde.github.io/Quickcart-pro/)

## 📝 License

This project is for educational purposes as a college submission.

---

## 🏆 Acknowledgments

- Firebase for backend services
- Bootstrap for responsive framework
- Font Awesome for icons
- Unsplash for placeholder images

---

**⭐ Star this repository if you found it helpful!**
