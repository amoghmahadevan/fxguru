import React from 'react';
import gitlogo from '../github-logo.png'
function Footer() {
  return (
    <div id = "footer" className = "footerlink"> 
        <span> 
            {"Made by Amogh Mahadevan   "}
        </span>
        <a href = {"https://github.com/amoghmahadevan"} target = "_blank" rel="noreferrer"> 
                <img className = "githublogo" src = {gitlogo} alt = {"Github Logo"}/>
            </a> 
    </div>
  )
}

export default Footer
