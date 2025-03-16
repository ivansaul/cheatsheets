import re


def define_env(env):
    @env.macro
    def prepend_base_path(file_path, base_path):
        """
        Reads a Markdown file and updates relative links by prepending a base path.

        Parameters:
        - file_path (str): Path to the Markdown file containing links.
        - base_path (str): Prefix to be added to relative links.

        Behavior:
        - Modifies only relative Markdown links (e.g., `[Text](path/)` → `[Text](base_path/path/)`).
        - Leaves absolute URLs (`http://...`, `https://...`) unchanged.

        Example:
        If the file contains:
            - [Python](python/)
            - [JavaScript](javascript/)
            - [External](https://example.com)

        Calling `prepend_base_path("src/en/docs/quick-ref/index.md", "quick-ref/")` results in:
            - [Python](quick-ref/python/)
            - [JavaScript](quick-ref/javascript/)
            - [External](https://example.com)
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
        except FileNotFoundError:
            return f"⚠ Error: File '{file_path}' not found."

        pattern = re.compile(r"(\[.*?\])\((?!https?:\/\/)(.*?)\)")

        updated_content = pattern.sub(rf"\1({base_path}\2)", content)

        return updated_content
