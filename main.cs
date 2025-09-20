using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Speech.Synthesis;
using System.Text;
using System.Windows.Forms;

namespace WordLearningApp
{
    class Program
    {
        private static SpeechSynthesizer synthesizer;
        private static Random random;

        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            synthesizer = new SpeechSynthesizer();
            random = new Random();

            List<string> content = LoadWordsFromFile();
            if (content == null || content.Count == 0)
                return;

            RunLearningSession(content);
        }

        private static List<string> LoadWordsFromFile()
        {
            string filePath;
            List<string> content = new List<string>();

            while (true)
            {
                using (OpenFileDialog openFileDialog = new OpenFileDialog())
                {
                    openFileDialog.Title = "Введите путь к файлу:";
                    openFileDialog.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*";

                    if (openFileDialog.ShowDialog() != DialogResult.OK)
                    {
                        MessageBox.Show("Файл не найден, попробуйте снова", "Ошибка",
                                       MessageBoxButtons.OK, MessageBoxIcon.Warning);
                        continue;
                    }

                    filePath = openFileDialog.FileName;
                }

                try
                {
                    string[] lines = File.ReadAllLines(filePath, Encoding.UTF8);

                    foreach (string line in lines)
                    {
                        if (line == " ")
                            continue;

                        string[] words = line.Split(new char[] { ' ', '\t' },
                                                   StringSplitOptions.RemoveEmptyEntries);

                        if (words.Length > 1)
                        {
                            foreach (string word in words)
                            {
                                string cleanWord = word.Trim().ToLower();
                                if (cleanWord.Length > 1 && cleanWord != "nh")
                                {
                                    content.Add(DeleteBadSignsFromWords(cleanWord));
                                }
                            }
                        }
                        else
                        {
                            string cleanLine = line.Trim().ToLower();
                            if (!string.IsNullOrEmpty(cleanLine))
                            {
                                content.Add(DeleteBadSignsFromWords(cleanLine));
                            }
                        }
                    }
                    break;
                }
                catch (FileNotFoundException)
                {
                    MessageBox.Show("Файл не найден, попробуйте снова", "Ошибка",
                                   MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    MessageBox.Show($"Произошла ошибка: {ex.Message}", "Ошибка",
                                   MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }

            return content;
        }

        private static string DeleteBadSignsFromWords(string word)
        {
            string badChars = "!\"#$%&()*+,-./:;<]^_`|~";
            foreach (char c in badChars)
            {
                word = word.Replace(c.ToString(), "");
            }
            return word;
        }

        private static void RunLearningSession(List<string> words)
        {
            List<string> errors = new List<string>();
            DateTime start = DateTime.Now;
            List<int> seenWords = new List<int>();

            Console.WriteLine("=== Начало обучения ===");
            Console.WriteLine("Введите 'след' для пропуска слова");
            Console.WriteLine("Нажмите Enter после ввода каждого слова");
            Console.WriteLine();

            for (int j = 0; j < words.Count; j++)
            {
                TimeSpan elapsed = DateTime.Now - start;
                int i;

                // Выбираем случайное слово, которое еще не было показано
                do
                {
                    i = random.Next(0, words.Count);
                } while (seenWords.Contains(i));

                seenWords.Add(i);
                int left = words.Count - j;

                // Произносим слово
                synthesizer.Speak(words[i]);

                Console.WriteLine($"Words: {words.Count}, words left: {left}, time: {elapsed.TotalSeconds:F1}s");
                Console.Write("Введите слово: ");

                string input = Console.ReadLine()?.Trim() ?? "";

                if (input == words[i])
                {
                    Console.WriteLine("Correct!");
                    Console.WriteLine();
                }
                else if (input == "след")
                {
                    Console.WriteLine("Пропущено");
                    Console.WriteLine($"Правильное слово: {words[i]}");
                    Console.WriteLine();
                    continue;
                }
                else
                {
                    synthesizer.Speak("Неправильно!");
                    Console.WriteLine("Incorrect!");
                    Console.WriteLine($"The correct word is: {words[i]}");
                    Console.WriteLine();
                    errors.Add(words[i]);
                }
            }

            // Показываем ошибки
            if (errors.Count > 0)
            {
                Console.WriteLine("=== Слова с ошибками ===");
                foreach (string error in errors)
                {
                    Console.WriteLine(error);
                }
            }
            else
            {
                Console.WriteLine("=== Отлично! Все слова правильные! ===");
            }

            Console.WriteLine("\nНажмите любую клавишу для выхода...");
            Console.ReadKey();

            synthesizer.Dispose();
        }
    }
}
