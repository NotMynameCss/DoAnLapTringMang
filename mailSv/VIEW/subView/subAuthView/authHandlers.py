from tkinter import messagebox

def handle_login_response(main_view, username):
    messagebox.showinfo("Đăng nhập", "Đăng nhập thành công")
    main_view.show_mail_view(username)

def handle_register_response(response):
    if response == "Đăng ký thành công":
        messagebox.showinfo("Đăng ký", "Đăng ký thành công")
    else:
        messagebox.showerror("Đăng ký", response)
