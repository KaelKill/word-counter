import unittest
import subprocess
import tkinter as tk
from tkinter import ttk
from count_words import count_words, remove_punctuation


class TestWordCounter(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_single_word(self):
        self.assertEqual(count_words("Hello"), 1)
        
    def test_multiple_words(self):
        self.assertEqual(count_words("Hello world! This is a test."), 6)
        
    def test_with_punctuation(self):
        self.assertEqual(count_words("Hello, world... How's it going?"), 5)
        
    def test_multiple_spaces_between_words(self):
        self.assertEqual(count_words("Hello    world"), 2)
        
    def test_only_punctuation(self):
        self.assertEqual(count_words("!!!...,,,???"), 0)
        
    def test_large_text(self):
        text = "This is a large test. " * 1000
        self.assertEqual(count_words(text), 5000)
        
    def test_leading_trailing_spaces(self):
        self.assertEqual(count_words("   Hello world   "), 2)

    def test_mixed_case(self):
        self.assertEqual(count_words("HELLO hello HeLLo"), 3)

class TestPunctuationRemover(unittest.TestCase):
    
    def test_remove_punctuation_empty_string(self):
        self.assertEqual(remove_punctuation(""), "")

    def test_remove_punctuation_no_punctuation(self):
        self.assertEqual(remove_punctuation("Hello world"), "Hello world")

    def test_remove_punctuation_with_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")

    def test_remove_punctuation_only_punctuation(self):
        self.assertEqual(remove_punctuation("!!!...,,,???"), "")

    def test_remove_punctuation_mixed_content(self):
        self.assertEqual(remove_punctuation("Hello, world... How's it going?"), "Hello world Hows it going")

class TestMainCLI(unittest.TestCase):

    def test_text_input(self):
        result = subprocess.run(['python', 'main.py', 'Hello world'], capture_output=True, text=True)
        self.assertIn("Word count: 2", result.stdout)

    def test_file_input(self):
        with open('test_file.txt', 'w') as f:
            f.write('Hello world, from python!')
        result = subprocess.run(['python', 'main.py', '--file', 'test_file.txt'], capture_output=True, text=True)
        self.assertIn("Word count: 4", result.stdout)

    def test_no_input(self):
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        self.assertIn("Please provide either text or a file to count words in.", result.stdout)

class TestTkinterInterface(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.text_input = tk.Text(self.root, height=5, width=40)
        self.text_input.pack()
        self.result_label = ttk.Label(self.root, text="Word count: 0")
        self.result_label.pack()
        self.count_button = ttk.Button(self.root, text="Count Words", command=self.count_words)
        self.count_button.pack()

    def tearDown(self):
        self.root.destroy()

    def count_words(self):
        text = self.text_input.get("1.0", tk.END)
        word_count = count_words(text)
        self.result_label.config(text=f"Word count: {word_count}")

    def test_empty_text(self):
        self.text_input.insert("1.0", "")
        self.count_button.invoke()
        self.assertEqual(self.result_label.cget("text"), "Word count: 0")

    def test_single_word(self):
        self.text_input.insert("1.0", "Hello")
        self.count_button.invoke()
        self.assertEqual(self.result_label.cget("text"), "Word count: 1")

    def test_multiple_words(self):
        self.text_input.insert("1.0", "Hello world! This is a test.")
        self.count_button.invoke()
        self.assertEqual(self.result_label.cget("text"), "Word count: 6")

    def test_with_punctuation(self):
        self.text_input.insert("1.0", "Hello, world... How's it going?")
        self.count_button.invoke()
        self.assertEqual(self.result_label.cget("text"), "Word count: 5")

    def test_multiple_spaces_between_words(self):
        self.text_input.insert("1.0", "Hello    world")
        self.count_button.invoke()
        self.assertEqual(self.result_label.cget("text"), "Word count: 2")

if __name__ == '__main__':
    unittest.main()