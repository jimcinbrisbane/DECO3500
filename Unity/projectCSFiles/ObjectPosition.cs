using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectPosition : MonoBehaviour
{
    //Ref - https://www.youtube.com/watch?v=9eTZqxxgGz8

    public GameObject vCam;
    public GameObject LookCube;
    public float speed;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        LookCube.transform.position = Vector3.MoveTowards(LookCube.transform.position, vCam.transform.position, speed);
    }
}
