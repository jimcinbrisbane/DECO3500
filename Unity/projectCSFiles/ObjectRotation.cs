using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectRotation : MonoBehaviour
{
    public GameObject targetCube;
    public float speed;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 targetDirection = targetCube.transform.position - transform.position;

        float singleStep = speed * Time.deltaTime;

        Vector3 newDirection = Vector3.RotateTowards(transform.forward, targetDirection, singleStep, 0.0f);

        //see for rest of the instructions https://docs.unity3d.com/ScriptReference/Vector3.RotateTowards.html
    }
}
