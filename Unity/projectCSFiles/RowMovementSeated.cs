using System.Collections;
using System.Collections.Generic;
using System.Net;
//using UnityEditor.Experimental.GraphView;
using UnityEngine;

public class RowMovementSeated : MonoBehaviour
{
    //Ref - https://www.youtube.com/watch?v=vua2a_Z3zlY

    public Transform rower;
    public Transform frontPoint;
    public Transform backPoint;
    Animator anim;
    public float speed;
    int direction = 1;

    private void Awake()
    {
        anim = GetComponent<Animator>();

    }

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        Vector3 target = currentMovementTarget();

        rower.position = Vector3.Lerp(rower.position, target, (anim.speed*2.2f)*Time.deltaTime);

        float distance = (target - (Vector3)rower.position).magnitude;

        if (distance <=0.1f)
        {
            direction *= -1;
        }
    }

    Vector3 currentMovementTarget()
    {
        if(direction == 1)
        {
            return frontPoint.position;
        } else
        {
            return backPoint.position;
        }
    }
}
