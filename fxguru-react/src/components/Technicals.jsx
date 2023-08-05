import React from 'react'
import Progress from './Progress'

const HEADERS = [
    "S3", "S2", "S1",
    "R1", "R2", "R3",
    "percent_bullish", "percent_bearish",
    "pivot", "studies_summary_color"
]
function Technicals({data}) {
  return (
    <div className = 'segment'>
        <Progress title = "Bullish" color = "#21ba45" percentage = {data.percent_bullish} />
        <Progress title = "Bearish" color = "#db2828" percentage = {data.percent_bearish} />
        <table>
            <thead>
                <tr> 
                    {
                        HEADERS.map(item => {
                            if(item == "studies_summary_color"){
                                return <th key = {item}> Summary </th>
                            }
                            else if(item == "percent_bearish"){
                                return <th key = {item}> Bearish Sentiment </th>
                            }
                            else if(item == "percent_bullish"){
                                return <th key = {item}> Bullish Sentiment </th>
                            }
                            else if(item == "pivot"){
                                return <th key = {item}> Pivot Points </th>
                            }
                            else{
                                return <th key = {item}> {item} </th>
                            }
                        })
                    }
                </tr>
                <tr> 
                    {
                        HEADERS.map(item => {
                            return <td key = {item}> {data[item]} </td>
                        })
                    }
                </tr>
            </thead>
        </table>
    </div>
  )
}

export default Technicals