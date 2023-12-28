import React from 'react'
import './Page.css'

export const Page = () => {
  return (
    <div className='container'>
        <h2> Image Compression </h2>
        <div className='upload'>
            Upload Image<br/>
            <input type='file' accept='image' className='btn'/>
        </div>
        <div className='view' >
            View Image <br/>
            <input type='file' accept='image' className='btn'/>
        </div>
    </div>
  )
}
