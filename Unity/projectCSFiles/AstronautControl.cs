using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AstronautControl : MonoBehaviour
{
    public GameObject target;
    public GameObject astronaut;
    public AudioSource source;
    public AudioClip clip;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        transform.Rotate(12f * Time.deltaTime, 10f * Time.deltaTime, 20f * Time.deltaTime, Space.Self);
        //Debug.Log("000 distance: " + Vector3.Distance(target.transform.position, astronaut.transform.position));
        if (Vector3.Distance(target.transform.position, astronaut.transform.position) < 8)
        {
            transform.localScale += new Vector3(-0.01f, -0.01f, -0.01f);
        }

        if (Vector3.Distance(target.transform.position, astronaut.transform.position) <= 3.5)
        {
            source.PlayOneShot(clip);
        }

        if (Vector3.Distance(target.transform.position, astronaut.transform.position) <= 2)
        {
            Destroy(astronaut);
        }


    }
}
