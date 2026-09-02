const registerForm = document.querySelector("#registerForm");

registerForm.addEventListener("submit", function (event) {

    // Form ko abhi submit hone se rokna
    event.preventDefault();

    // Input values lena
    const name = document.querySelector("#name").value.trim();
    const email = document.querySelector("#email").value.trim();
    const password = document.querySelector("#password").value;
    const confirmPassword =
        document.querySelector("#confirm-password").value;


    // =========================
    // Name Validation
    // =========================

    if (name === "") {
        alert("Name is required.");
        return;
    }

    // Sirf letters aur spaces allow
    const namePattern = /^[A-Za-z ]+$/;

    if (!namePattern.test(name)) {
        alert("Name can only contain letters and spaces.");
        return;
    }


    // =========================
    // Email Validation
    // =========================

    if (email === "") {
        alert("Email is required.");
        return;
    }

    const emailPattern =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }


    // =========================
    // Password Validation
    // =========================

    if (password === "") {
        alert("Password is required.");
        return;
    }

    if (password.length < 8) {
        alert("Password must be at least 8 characters.");
        return;
    }

    if (!/[A-Z]/.test(password)) {
        alert("Password must contain an uppercase letter.");
        return;
    }

    if (!/[a-z]/.test(password)) {
        alert("Password must contain a lowercase letter.");
        return;
    }

    if (!/[0-9]/.test(password)) {
        alert("Password must contain a number.");
        return;
    }

    if (!/[!@#$%^&*]/.test(password)) {
        alert("Password must contain a special character.");
        return;
    }


    // =========================
    // Confirm Password
    // =========================

    if (confirmPassword === "") {
        alert("Please confirm your password.");
        return;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
    }


    // =========================
    // Success
    // =========================

    alert("Registration successful!");

});
// =========================
// Password Show / Hide
// =========================

const password = document.querySelector("#password");
const togglePassword = document.querySelector("#togglePassword");

togglePassword.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";

    } else {

        password.type = "password";

    }

});
const confirmPassword =
    document.querySelector("#confirm-password");

const toggleConfirmPassword =
    document.querySelector("#toggleConfirmPassword");


toggleConfirmPassword.addEventListener("click", function () {

    if (confirmPassword.type === "password") {

        confirmPassword.type = "text";

    } else {

        confirmPassword.type = "password";

    }

});