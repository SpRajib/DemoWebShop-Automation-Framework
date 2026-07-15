# Demo Web Shop Automation - Test Cases

## Project
**Application:** Demo Web Shop  
**URL:** https://demowebshop.tricentis.com/  
**Automation Tool:** Selenium WebDriver  
**Language:** Python  
**Framework:** Pytest  
**Design Pattern:** Page Object Model (POM)

---

# Module 1: User Registration

### TC_REG_001 - Verify Successful User Registration

**Priority:** High

**Precondition**
- User is on the Demo Web Shop homepage.

**Test Steps**

1. Open the application.
2. Click **Register**.
3. Select Gender.
4. Enter First Name.
5. Enter Last Name.
6. Enter a unique Email Address.
7. Enter Password.
8. Confirm Password.
9. Click **Register**.

**Expected Result**

- User registration is completed successfully.
- Success message is displayed.

---

### TC_REG_002 - Verify Registration with Existing Email

**Priority:** High

**Precondition**

- Existing account already registered.

**Test Steps**

1. Open Register page.
2. Enter valid details.
3. Enter an already registered Email.
4. Click Register.

**Expected Result**

- Registration should fail.
- Appropriate error message should be displayed.

---

### TC_REG_003 - Verify Mandatory Field Validation

**Priority:** Medium

**Test Steps**

1. Open Register page.
2. Leave all fields blank.
3. Click Register.

**Expected Result**

- Validation messages should appear for mandatory fields.

---

# Module 2: Login

### TC_LOG_001 - Verify Login with Valid Credentials

**Priority:** High

**Precondition**

- User account already exists.

**Test Steps**

1. Open Login page.
2. Enter valid Email.
3. Enter valid Password.
4. Click Login.

**Expected Result**

- User should be logged in successfully.

---

### TC_LOG_002 - Verify Login with Invalid Password

**Priority:** High

**Test Steps**

1. Open Login page.
2. Enter valid Email.
3. Enter invalid Password.
4. Click Login.

**Expected Result**

- Login should fail.
- Error message should be displayed.

---

### TC_LOG_003 - Verify Login with Empty Credentials

**Priority:** Medium

**Test Steps**

1. Open Login page.
2. Leave Email blank.
3. Leave Password blank.
4. Click Login.

**Expected Result**

- Validation or login error should be displayed.

---

### TC_LOG_004 - Verify User Logout

**Priority:** High

**Precondition**

- User is logged in.

**Test Steps**

1. Click Logout.

**Expected Result**

- User should be logged out successfully.

---

# Module 3: Product Search

### TC_SEARCH_001 - Search Existing Product

**Priority:** High

**Test Steps**

1. Enter "Laptop" in Search box.
2. Click Search.

**Expected Result**

- Matching products should be displayed.

---

### TC_SEARCH_002 - Search Non-Existing Product

**Priority:** Medium

**Test Steps**

1. Enter random product name.
2. Click Search.

**Expected Result**

- "No products were found" message should be displayed.

---

### TC_SEARCH_003 - Empty Search

**Priority:** Low

**Test Steps**

1. Leave Search box empty.
2. Click Search.

**Expected Result**

- Search page should open or display all products according to application behavior.

---

# Module 4: Add Product to Cart

### TC_CART_001 - Add Product to Cart

**Priority:** High

**Precondition**

- Product is available.

**Test Steps**

1. Search product.
2. Open Product.
3. Click Add to Cart.

**Expected Result**

- Product should be added to shopping cart.

---

### TC_CART_002 - Verify Shopping Cart Count

**Priority:** Medium

**Test Steps**

1. Add one product.

**Expected Result**

- Shopping cart count should increase.

---

# Module 5: Remove Product from Cart

### TC_REMOVE_001 - Remove Product

**Priority:** High

**Precondition**

- Product already exists in cart.

**Test Steps**

1. Open Shopping Cart.
2. Select Remove checkbox.
3. Click Update Cart.

**Expected Result**

- Product should be removed successfully.

---

### TC_REMOVE_002 - Verify Empty Cart Message

**Priority:** Medium

**Test Steps**

1. Remove all products.

**Expected Result**

- Shopping cart should display empty message.

---

# Module 6: Checkout

### TC_CHECKOUT_001 - Successful Checkout

**Priority:** High

**Precondition**

- User is logged in.
- Product exists in cart.

**Test Steps**

1. Open Shopping Cart.
2. Click Checkout.
3. Fill Billing Address.
4. Continue.
5. Select Shipping Method.
6. Continue.
7. Select Payment Method.
8. Continue.
9. Confirm Order.

**Expected Result**

- Order should be placed successfully.
- Order confirmation message should be displayed.

---

### TC_CHECKOUT_002 - Checkout with Empty Cart

**Priority:** Medium

**Test Steps**

1. Open Shopping Cart.
2. Click Checkout.

**Expected Result**

- Checkout should not proceed.
- Appropriate message should be displayed.

---

# Module 7: Product Review

### TC_REVIEW_001 - Verify User Can Submit Product Review

**Priority:** High

**Precondition**

- User is logged in.
- Product exists.

**Test Steps**

1. Login to the application.
2. Search for a product.
3. Open the product details page.
4. Click **Add your review**.
5. Enter Review Title.
6. Enter Review Text.
7. Select Rating (1–5).
8. Click **Submit Review**.

**Expected Result**

- Review should be submitted successfully.
- Success message should be displayed.

---

### TC_REVIEW_002 - Verify Product Review Without Login

**Priority:** High

**Precondition**

- User is not logged in.

**Test Steps**

1. Open any product.
2. Click **Add your review**.
3. Try to submit a review.

**Expected Result**

- User should be redirected to the Login page or prompted to log in.

---

### TC_REVIEW_003 - Verify Mandatory Fields in Product Review

**Priority:** Medium

**Precondition**

- User is logged in.

**Test Steps**

1. Open Product Review page.
2. Leave Review Title blank.
3. Leave Review Text blank.
4. Do not select a rating (if applicable).
5. Click **Submit Review**.

**Expected Result**

- Validation messages should be displayed for required fields.

---

### TC_REVIEW_004 - Verify Review Rating Selection

**Priority:** Medium

**Precondition**

- User is logged in.

**Test Steps**

1. Open Product Review page.
2. Select each rating option (1 to 5 stars).
3. Submit a valid review.

**Expected Result**

- Selected rating should be saved with the review.

---

### TC_REVIEW_005 - Verify Submitted Review Appears in Product Reviews

**Priority:** High

**Precondition**

- User has submitted a review.

**Test Steps**

1. Submit a valid review.
2. Refresh the product page.
3. Navigate to the Product Reviews section.

**Expected Result**

- Newly submitted review should be visible in the list of reviews.

# Test Summary

| Module | Total Test Cases |
|---------|------------------:|
| Registration | 3 |
| Login | 4 |
| Search | 3 |
| Add to Cart | 2 |
| Remove from Cart | 2 |
| Checkout | 2 |
| Contact Us | 2 |
| **Total** | **18** |

---

## Test Environment

| Item | Details |
|------|---------|
| Browser | Google Chrome (Latest) |
| Operating System | Windows 11 / macOS |
| Automation Tool | Selenium WebDriver |
| Language | Python 3.x |
| Framework | Pytest |
| Design Pattern | Page Object Model (POM) |