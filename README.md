# 🚀 اس ام اس بمبر ایرانی(SMS Bomber Tester IRAN)

**توضیح:** این ابزار یک اسکریپت پایتونی برای ارسال تعداد زیادی پیامک به یک شماره خاص با استفاده از APIهای مختلف است. هدف این پروژه صرفاً آموزشی بوده و برای بررسی نحوه عملکرد چنین ابزارهایی طراحی شده است.

## ⚠️ مسئولیت و هشدار قانونی
این نرم‌افزار **فقط برای اهداف تحقیقاتی و آموزشی** ارائه شده است. هرگونه استفاده غیرمجاز، از جمله اسپم، آزار و اذیت یا فعالیت‌های غیرقانونی، **اکیداً ممنوع** است. استفاده نادرست از این ابزار، مسئولیت کامل آن بر عهده کاربر خواهد بود.

## ✨ ویژگی‌ها
- ارسال پیامک‌های متعدد به یک شماره خاص
- استفاده از APIهای مختلف برای افزایش تنوع منابع پیامک
- رابط کاربری کنسولی ساده و نمایش پیشرفت در زمان اجرا
- مدیریت خطاها و نمایش وضعیت هر درخواست

## 🛠️ پیش‌نیازها
برای اجرای این ابزار، نیاز به **Python 3.x** و نصب کتابخانه‌های زیر دارید:
- `requests` (برای ارسال درخواست‌های HTTP)
- `fake-useragent` (برای ایجاد هدرهای تصادفی)
- `rich` (برای نمایش خروجی‌های زیباتر در کنسول)

**نصب وابستگی‌ها:**
```bash
pip install -r requirements.txt
```

## 🚀 نحوه استفاده
1. ریپازیتوری را کلون کنید:
   ```bash
   git clone https://github.com/WolfAlicode/sms-spam-tester.git
   ```
2. وارد پوشه پروژه شوید:
   ```bash
   cd sms-bomber
   ```
3. اسکریپت را اجرا کنید:
   ```bash
   python main.py
   ```
4. شماره هدف را وارد کنید (فرمت: `09********`).
5. تعداد درخواست‌های موردنظر را مشخص کنید.

## 🎯 نحوه کار
اسکریپت با اجرای همزمان چندین درخواست API، پیامک‌ها را ارسال کرده و میزان موفقیت را گزارش می‌کند.

## 💡 مشارکت
اگر ایده یا اصلاحاتی برای این پروژه دارید:
- یک **Issue** در گیت‌هاب باز کنید.
- یک **Pull Request** ارسال کنید.

## 📝 مجوز
این پروژه تحت **مجوز GPL v3.0** منتشر شده است، به این معنی که استفاده، تغییر و توزیع آن **آزاد** است، اما هرگونه تغییر باید تحت همین مجوز بماند.

---
❗ **توجه:**  این ابزار برای بررسی مسائل امنیتی در سیستم‌های احراز هویت پیامکی طراحی شده است. لطفاً آن را **به‌صورت مسئولانه** و تنها در **موارد مجاز و قانونی** استفاده کنید.(و در صورت درخواست هر کدوم از API ها اون بخش از کد پاک خواهد شد)

# SMS Bomber Tester IRAN

**SMS Bomber** is a Python-based tool designed to demonstrate the concept of sending multiple SMS messages to a specified phone number using various APIs. This project is intended for **educational purposes only**, to explore how such tools function and to emphasize the importance of **security, privacy, and ethical considerations** in digital communications.

## ⚠️ Disclaimer

**Important:** This software is provided for **educational and research purposes only**. The use of this software for any malicious activities, such as **spamming, harassment, or any other illegal actions, is strictly prohibited**. The author is **not responsible** for any misuse or damage caused by this software. Always ensure you have **explicit permission** from the recipient before sending any messages.

## ✨ Features

- Sends multiple SMS messages to a specified phone number.  
- Leverages a variety of APIs to diversify message sources.  
- Offers a **user-friendly console interface** with real-time progress tracking.  
- Handles errors gracefully and provides feedback on the success or failure of API calls.  
- Executes API calls concurrently for efficiency, using Python's threading capabilities.  

## 📌 Requirements

To run this project, you need **Python 3.x** and the following libraries:

- `requests`: For making HTTP requests to APIs.  
- `fake-useragent`: For generating random user agents to enhance anonymity and avoid detection.  
- `rich`: For enhanced console output formatting, including progress bars and styled text.  

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

The project includes a script that automatically checks for and installs these dependencies when you run the main program.

## 🚀 Usage

Follow these steps to set up and run the **SMS Bomber**:

### Clone the Repository:
```bash
git clone https://github.com/WolfAlicode/sms-spam-tester.git
```

### Navigate to the Project Directory:
```bash
cd sms-bomber
```

### Run the Script:
```bash
python main.py
```

### Provide Input:
- When prompted, enter the target phone number in the format **09**********.  
- Specify the total number of API calls you want to make.  

### Monitor Progress:
- The script will execute the API calls concurrently and display a **progress bar** with real-time updates.  
- Upon completion, it will report the number of successful API calls.  

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please consider the following:

- **Open an Issue**: Discuss your suggestions or report problems on the GitHub repository.  
- **Submit a Pull Request**: Fork the repository, make your changes, and submit a pull request. Ensure your code adheres to the project's coding standards and the **GNU GPL license**.  

All contributions should **respect the ethical guidelines** outlined in the Disclaimer section.

## 📜 License

This project is licensed under the **GNU General Public License v3.0**. This means:

- You are free to **use, modify, and distribute** this software.  
- Any modifications or distributions **must also be licensed under the GNU GPL**, ensuring the software remains free and open-source.  
- There is **no warranty** provided with this software.  

For the full license text, see the `LICENSE` file in the repository or visit [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## 📬 Contact

If you encounter issues, have questions, or want to provide feedback, please:

- Open an issue on the **GitHub repository**.  
- Contact the maintainer at **[farisatali12@gmail.com](mailto:your-email@example.com)**.  

## 🔍 Additional Notes

- **Ethical Use**: This tool is designed to educate users about API interactions and the potential vulnerabilities in SMS-based systems. Always **use it responsibly and with consent**.  
- **Technology Stack**: The project leverages Python's `ThreadPoolExecutor` for concurrent API calls, enhancing performance while maintaining simplicity.  
- **Customization**: Feel free to **adapt the code** for your educational experiments, keeping in mind the **licensing and ethical constraints**.  

Thank you for exploring this project! We hope it serves as a valuable learning resource. 🚀
