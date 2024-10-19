using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;
using static Unity.VisualScripting.Member;

public class ObjectTravel : MonoBehaviour
{
    //Ref - https://www.youtube.com/watch?v=9eTZqxxgGz8

    public GameObject shark;
    public GameObject SharkCube;
    public float sharkSpeed;
    private Vector3 startPos;

    // Start is called before the first frame update
    void Start()
    {
       
    }

    // Update is called once per frame
    void Update()
    {
        if (shark.IsDestroyed())
        {
            Instantiate(shark);
        }

        shark.transform.position = Vector3.MoveTowards(shark.transform.position, SharkCube.transform.position, sharkSpeed);

        if (Vector3.Distance(SharkCube.transform.position, shark.transform.position) < 10)
        {
            transform.localScale += new Vector3(-0.0001f, -0.0001f, -0.0001f);
        }

        if (Vector3.Distance(SharkCube.transform.position, shark.transform.position) <= 2)
        {
            Destroy(shark);
        }
    }
}
