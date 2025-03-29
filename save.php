<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    try {
        $db = new PDO("sqlite:database.db");
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // استلام البيانات من النموذج
        $username = $_POST['username'];
        $email = $_POST['email'];
        $password = password_hash($_POST['password'], PASSWORD_BCRYPT); // تشفير كلمة المرور

        // إدخال البيانات في قاعدة البيانات
        $stmt = $db->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
        $stmt->execute([$username, $email, $password]);

        echo "تم التسجيل بنجاح!";
    } catch (PDOException $e) {
        echo "خطأ: " . $e->getMessage();
    }
}
?>
