# Password Generate

A robust and user-friendly Python utility for generating secure, customizable passwords with extensive configuration options.

## Features

- **Secure Generation**: Creates cryptographically secure random passwords
- **Highly Customizable**: Configure character sets, length, and complexity requirements
- **Multiple Character Types**: Support for uppercase, lowercase, digits, and special characters
- **Flexible Options**: Include or exclude specific character types as needed
- **Lightweight**: Minimal dependencies for easy integration

## Installation

### Requirements
- Python 3.6 or higher

### Setup

Clone the repository:
```bash
git clone https://github.com/Abu-Bakar-Rakib/password-generate.git
cd password-generate
```

## Usage

### Basic Example

```python
from password_generate import PasswordGenerator

# Create a password generator instance
generator = PasswordGenerator()

# Generate a simple password
password = generator.generate()
print(password)
```

### Advanced Configuration

```python
from password_generate import PasswordGenerator

# Create generator with custom settings
generator = PasswordGenerator(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_special=True
)

# Generate multiple passwords
for _ in range(5):
    password = generator.generate()
    print(password)
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `length` | int | 12 | Password length |
| `use_uppercase` | bool | True | Include uppercase letters (A-Z) |
| `use_lowercase` | bool | True | Include lowercase letters (a-z) |
| `use_digits` | bool | True | Include digits (0-9) |
| `use_special` | bool | True | Include special characters |

## Project Structure

```
password-generate/
├── README.md
└── password_generate.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request with improvements or bug fixes.

### Steps to Contribute

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions, please open an [issue](https://github.com/Abu-Bakar-Rakib/password-generate/issues) on GitHub.

## Author

**Abu Bakar Rakib**

- GitHub: [@Abu-Bakar-Rakib](https://github.com/Abu-Bakar-Rakib)

---
