using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectAudioTrigger : MonoBehaviour
{
    public GameObject vCam;
    public GameObject shark;
    public AudioSource source;
    public AudioClip clip;
    public float distance;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Vector3.Distance(vCam.transform.position, shark.transform.position) <= distance)
        {
            source.PlayOneShot(clip);
        }
    }
}
