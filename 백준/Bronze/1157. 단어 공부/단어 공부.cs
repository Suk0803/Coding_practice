using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main()
        {
            int[] counts = new int[26];

            string line = Console.ReadLine().ToUpper();
            foreach(char c in line)
            {
                counts[c - 'A']++;
            }

            int max = int.MinValue;
            int maxIndex = -1;
            bool duplicated = false;
            for(int i = 0; i < counts.Length; i++)
            {
                if (counts[i] > max)
                {
                    max = counts[i];
                    maxIndex = i;
                    duplicated = false;
                }
                else if (counts[i] == max)
                {
                    duplicated = true;
                }
            }

            Console.WriteLine(duplicated == true ? '?' : (char)(maxIndex + 'A'));
        }
    }
}