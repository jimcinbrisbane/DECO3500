//using Palmmedia.ReportGenerator.Core.Parser.Analysis;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using TMPro;
using UnityEditor;
using UnityEngine;

public class AnimationSpeed : MonoBehaviour
{
    //Ref - https://www.youtube.com/watch?v=QmCwVEFW0aE
    //Ref - https://www.youtube.com/watch?v=sXjhwKPoEVA&t=100s

    Animator anim;
    private string filePath;
    private int currentLineIndex = 0;
    //[SerializeField] private TextMeshProUGUI myText;
    public float transitionInterval; //3f given data.


    // Start is called before the first frame update
    void Start()
    {
        filePath = Application.dataPath + "/output.txt";
        InvokeRepeating("ChangeAnimationSpeed",1f, transitionInterval);
    }

    private void Awake()
    {
        anim = GetComponent<Animator>();

    }

    // Update is called once per frame
    void Update()
    {

    }

    void ChangeAnimationSpeed()
    {
        //myText.text = GetLineAtIndex(currentLineIndex);
        float rowSpeed = GetNumberAtIndex(currentLineIndex);
        anim.speed = rowSpeed; //will need to 'normalize unmbers (0= no movement, 1= normal, >2 = fast).
        //anim.speed = 1f;
        NextLineIndex();
    }

    private float GetNumberAtIndex(int index)
    {
        string[] lines = File.ReadAllLines(filePath);

        //clean and change to float here.
        if (index < lines.Length)
        {
            //take float after '-> '
            float speed = float.Parse(lines[index].Substring(15));
            speed = (speed/100)*1.7f;
            //Debug.Log("0001: " + speed);

            return speed; //don't return lines, lines will be a new variable in float.
        }
        else
        {
            //Run out of data, but keep going.
            return 1f;
        }
    }

    public void NextLineIndex()
    {
        currentLineIndex++;

    }

    
}
 
