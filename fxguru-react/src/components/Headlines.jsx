import React, { useEffect, useState } from 'react'
import TitleHeader from './TitleHeader'
import endPoints from '../app/api';
import Headline from './Headline';

function Headlines() {

  const [headlines, setHeadlines] = useState(null);

  useEffect(() => {
    loadHeadlines();
  }, [])

  const loadHeadlines = async () => {
      const data = await endPoints.headlines();
      setHeadlines(data);
  }

  return (
    <div>
        <TitleHeader title = "Headlines" />
        <div className="segment">
          {
            headlines && headlines.map((item, index) => {
              return <Headline key = {index} data = {item}/>
            })
          }
        </div>
    </div>
  )
}

export default Headlines