# Gravatar Image Fetcher

This Python script allows you to fetch and download the Gravatar image of a user based on their email address. The image is saved to a specified directory.

## Features

- Fetches Gravatar images based on the email address.
- Supports saving the image to a custom directory.
- Automatically creates the directory if it does not exist.
- Utilizes the MD5 hash of the email to access the Gravatar API.

## Prerequisites

Before running the script, make sure you have Python installed. Additionally, you'll need to install the `requests` library. You can install it using pip:

```bash
pip install requests
```

## Usage

To use the script, pass the email as an argument. You can also specify the directory where the image will be saved.

### Basic Example

To fetch the Gravatar image and save it in the default `./pictures` directory:

```bash
python gravatar.py user@domain.tld
```

### Specifying a Custom Directory

You can specify a different directory to save the image using the `--save-dir` option:

```bash
python gravatar.py user@domain.tld --save-dir ./my-directory
```

If the directory does not exist, it will be created automatically.

## Arguments

- `email`: The email address of the user for which to fetch the Gravatar image.
- `--save-dir`: (Optional) The directory where the Gravatar image will be saved. The default is `./pictures`.

## Example

```bash
python gravatar.py johndoe@example.com --save-dir ./avatars
```

This command will fetch the Gravatar image for `johndoe@example.com` and save it in the `./avatars` directory.

## How It Works

1. The email address is stripped of extra spaces and converted to lowercase.
2. An MD5 hash of the email is created.
3. The script constructs the Gravatar URL using the hashed email.
4. A GET request is sent to the Gravatar API to retrieve the image.
5. The image is saved to the specified directory with the name based on the MD5 hash of the email.

## License

This project is licensed under the MIT License.
```
