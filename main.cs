using System;

class MainClass 
{
  public static void Main (string[] args) 
  {
    Console.Write("please enter your desired height ");
    string strheight = Console.ReadLine();
    int height = int.Parse(strheight);
    for (int x = 1; x <= height; x++)
    {
      for (int i = 1; i <= x; i++)
      {
        Console.Write("*");
      }
      Console.WriteLine("");
    }
  }
}