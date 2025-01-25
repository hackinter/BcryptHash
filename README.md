আপনার লেখা বর্তমানে ভালোই ডিজাইন করা এবং টার্মিনাল আউটপুটের মতো আউটপুট প্রদর্শন করছে। তবে, আপনি যদি পুরোপুরি টার্মিনাল লুক অ্যান্ড ফিল চান, তাহলে কিছু ছোট ছোট পরিবর্তন করতে হবে। এখানে কিছু প্রস্তাবনা:

1. **Code block style**: টার্মিনাল আউটপুটের মতো দেখতে, কোড ব্লককে আরও অ্যাডভান্সড স্টাইল দেওয়া যায়। Markdown-এ আপনি `bash` কোড ব্লক ব্যবহার করতে পারেন, যা কিছুটা টার্মিনালের মতো দেখতে হবে।

2. **Font style**: `README.md` ফাইলের জন্য আপনি শুধু **monospace font** ব্যবহার করতে পারেন, যেটি টার্মিনাল লুক তৈরির জন্য আদর্শ।

এখন আমি কিছু পরিবর্তন করে দিচ্ছি যাতে আপনি পুরোপুরি টার্মিনাল স্টাইল পেতে পারেন।

### পরিবর্তিত `README.md` কোড:

```markdown
# BcryptHash 🔐

A simple Python-based tool to work with Bcrypt hashes. This tool allows users to generate random Bcrypt hashes, verify them, and even perform a brute force attack for educational purposes only. 🎓

<div align="center">
  <a href="https://github.com/hackinter/BcryptHash/releases">
    <img src="https://img.shields.io/badge/Version-1.0.1-blue.svg" alt="Version"> 
  </a>
  <a href="https://github.com/hackinter">
    <img src="https://img.shields.io/badge/GITHUB-HACKINTER-red.svg" alt="GitHub">
  </a>
</div>

## Features ✨
1. **Generate Random Bcrypt Hash**: Create a random Bcrypt hash from any password. 🔑
2. **Bcrypt Hash Verifier**: Verify if a given password matches a provided Bcrypt hash. ✅
3. **Bcrypt Hash Brute Force**: A brute force tool to try cracking a Bcrypt hash using a wordlist. This feature is strictly for educational purposes. ⚡
4. **Help**: Displays the help information for the tool. ❓
5. **Exit**: Exits the tool. 🚪

## Requirements 📋:
- Python 3.x 🐍
- `bcrypt` library (install using `pip install bcrypt`)

## Usage 📚:

1. Clone the repository:
   ```bash
   git clone https://github.com/hackinter/BcryptHash.git
   cd BcryptHash
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the tool:
   ```bash
   python3 Bcrypt.py
   ```

4. Follow the prompts in the terminal to use the tool's features.

## Example Output 🖥️:
### Generate a Random Bcrypt Hash
```bash
⚡ Please enter your password ⚡
Enter password: 
Login successful! 🎉
Welcome to the Bcrypt Tool

1. Generate a Random Bcrypt Hash
2. Bcrypt Hash Verifier
3. Bcrypt Hash Brute Force (Educational Purpose Only)
4. Help
5. Exit
Choose an option (1-5): 1
Enter a password to hash: loveyou
Generated Hash: $2b$12$96csxV6kfw2e4iARbqVW7uPSG9jf4BVchP5PpboaW4S8kp1Y2ryY2
```

### Bcrypt Hash Verifier
```bash
Welcome to the Bcrypt Tool

1. Generate a Random Bcrypt Hash
2. Bcrypt Hash Verifier
3. Bcrypt Hash Brute Force (Educational Purpose Only)
4. Help
5. Exit
Choose an option (1-5): 2
Enter the bcrypt hash: $2b$12$96csxV6kfw2e4iARbqVW7uPSG9jf4BVchP5PpboaW4S8kp1Y2ryY2
Enter the password to verify: loveyou
Password matches the hash!
```

### Bcrypt Hash Brute Force (Educational Purpose Only)
```bash
Welcome to the Bcrypt Tool

1. Generate Random Bcrypt Hash
2. Bcrypt Hash Verifier
3. Bcrypt Hash Brute Force (Educational Purpose Only)
4. Help
5. Exit
Choose an option (1-5): 3
This option is for educational purposes only.
Enter the bcrypt hash: $2b$12$96csxV6kfw2e4iARbqVW7uPSG9jf4BVchP5PpboaW4S8kp1Y2ryY2
Enter the path to the wordlist: /usr/share/wordlists/rockyou.txt
Starting brute force...
Attempting passwords:   0%|                                                     | 51/14344391 [00:09<743:33:06,  5.36password/s]
Password found: loveyou
```

## Brute Force (Educational Purpose Only) 🔓:

The brute force option is designed for educational purposes to demonstrate how password hashes can be cracked using a wordlist. Using strong and complex passwords to prevent brute-force attacks is highly recommended. 🛡️

**Disclaimer**: This tool is for educational purposes only. Use it responsibly and only on systems with explicit permission to test. 🚫

## License 📜
This project is licensed under the MIT License. See the [LICENSE](https://github.com/hackinter/BcryptHash/blob/main/LICENSE) file for more details.

## Contributing 🤝
We welcome contributions! If you'd like to contribute, you can fix the repository and submit a pull request. If you encounter any bugs or have suggestions, please open an issue.

## Contact 📧
For any queries or issues, feel free to reach out to us:

[![Email](https://img.shields.io/badge/HACKINTER-MAIL-red.svg)](mailto:ceh.ec.counselor147@gmail.com)  
[![Telegram](https://img.shields.io/badge/HACKINTER-T.ME-blue.svg)](https://t.me/chat_with_hackinter_bot)  
[![Twitter](https://img.shields.io/badge/HACKINTER-TWITTER-black.svg)](https://x.com/_anonix_z)  

## Author ✍️
- **HACKINTER** | [GitHub](https://github.com/hackinter)
