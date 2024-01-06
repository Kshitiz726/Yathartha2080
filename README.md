# Bulk Invitation Card Generator

**Description:**

This repository contains a Python script, `bulk_invitation.py`, which generates invitation cards in bulk using a template PSD file, an Excel sheet with names, and a custom font. The script uses the Pillow library (PIL) for image manipulation and requires the specified dependencies to function correctly.

**Requirements:**

- Python 3.8.12 
- pandas==1.5.2
- Pillow==9.4.0
- Excel file (`name_excel_sheet.xlsx`) with a column labeled "Name" containing the names for the invitations
- PSD template file (`invitation_card_template.psd`) for the invitation design
- TrueType Font file (`your_required_font.ttf`) for customizing the text style

**Usage:**

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Kshitiz726/event-card-creator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd event-card-creator 
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
**READ:** Make sure to adjust the path properly, you need to put all the files in root directory before using it, or give exact path of requirements.txt and same for all others, if they are in folder....

4. Place your Excel file (`name_excel_sheet.xlsx`), PSD template file (`invitation_card_template.psd`), and TrueType Font file (`your_required_font.ttf`) in the project directory.

5. Open the `bulk_invitation.py` script in a text editor and modify the following variables according to your setup:

    ```python
    folder_path = 'C:/Users/Kshitiz/Downloads/output'
    template_path = "invitation_card_template.psd"
    font_path = "your_required_font.ttf"
    ```

6. Run the script:

    ```bash
    python bulk_invitation.py
    ```

   The generated invitation cards will be saved in the specified output folder.

**Note:**

- Make sure to customize the folder path, template path, and font path in the `bulk_invitation.py` script before running it.
- Adjust the position, color, and other parameters in the script to match your desired design.
- Ensure that the PSD template, Excel file, and font file are formatted correctly for the script to work as intended.

Feel free to reach out if you have any questions or need assistance! You can contact me via my [Instagram](https://www.instagram.com/loosey_0000/) account.
