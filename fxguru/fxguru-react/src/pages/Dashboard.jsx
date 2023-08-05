import React, { useEffect, useState } from 'react'
import TitleHeader from '../components/TitleHeader'
import Select from '../components/Select'
import { COUNTS, GRANULARITIES, PAIRS } from '../app/data'
import Button from '../components/Button'
import endPoints from '../app/api'
import Technicals from '../components/Technicals'
import PriceChart from '../components/PriceChart'
function Dashboard() {

  const [selectedPair, setSelectedPair] = useState(null);
  const [selectedGranularity, setSelectedGranularity] = useState(null);
  const [technicalsData, setTechnicalsData] = useState(null);
  const [priceData, setPriceData] = useState(null);
  const [selectedCount, setSelectedCount] = useState(COUNTS[0].value);
  const [options, setOptions] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadOptions();
  }, []);

  const handleCountChange = (count) => {
    setSelectedCount(count);
    loadPrices(count);
  }

  const loadPrices = async(count) => {
    const data = await endPoints.prices(selectedPair, selectedGranularity, count);
    setPriceData(data);
  }

  const loadTechnicals = async () => {
    const data = await endPoints.technicals(selectedPair, selectedGranularity);
    setTechnicalsData(data);
    loadPrices(selectedCount);
  }

  const loadOptions = async() => {
    const data = await endPoints.options();
    setOptions(data);
    setSelectedGranularity(data.granularities[0].value)
    setSelectedPair(data.pairs[0].value)
    setLoading(false)
  }

  if(loading == true) return <h1> Loading... </h1>

  return (
    <div>
      <TitleHeader title = "Options"/>
      <div className = "segment options">
        <Select 
          name = "Currency Pairs" 
          title = "Select Currency Pair" 
          options = {options.pairs}
          defaultValue = {selectedPair}
          onSelected = {setSelectedPair}/>
        <Select 
          name = "Granularities" 
          title = "Select Granularity" 
          options = {options.granularities}
          defaultValue = {selectedGranularity}
          onSelected = {setSelectedGranularity}/>
        <Button text="Load" handleClick={() => loadTechnicals()}/>
      </div>
      <TitleHeader title = "Technicals" />
      {technicalsData && <Technicals data = {technicalsData} />}
      <TitleHeader title = "Price Chart" />
      {priceData && <PriceChart 
                      priceData = {priceData}
                      selectedPair = {selectedPair}
                      selectedGranularity = {selectedGranularity}
                      selectedCount = {selectedCount}
                      handleCountChange={handleCountChange}
                      />}
    </div>
  )
}

export default Dashboard