# SMS Bomber

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
