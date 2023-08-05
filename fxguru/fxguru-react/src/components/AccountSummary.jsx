import React, { useEffect, useState } from 'react'
import TitleHeader from './TitleHeader'
import endPoints from '../app/api';

const DATA_KEYS = [
    {name: "Account Number: ", key: "id", fixed: -1},
    {name: "Balance: ", key: "balance", fixed: -1},
    {name: "NAV: ", key: "NAV", fixed: -1},
    {name: "Open Trades: ", key: "openTradeCount", fixed: -1},
    {name: "Unrealized PL: ", key: "unrealizedPL", fixed: -1},
    {name: "Closeout Percentage: ", key: "marginCloseoutPercent", fixed: -1},
    {name: "Currency: ", key: "currency", fixed: -1},
    {name: "Last Transaction ID: ", key: "lastTransactionID", fixed: -1},
    {name: "Withdrawal Limit: ", key: "withdrawalLimit", fixed: -1},
]

function AccountSummary() {

  const [account, setAccount] = useState(null);

  useEffect(() => {
    loadAccount();
  }, [])

  const loadAccount = async () => {
      const data = await endPoints.account();
      setAccount(data);
  }

  return (
    <div>
      <TitleHeader title = "Account Summary" />
      {
        account && <div className = 'segment'> 
            {
              DATA_KEYS.map(item => {
                return <div key = {item.key} className = "account-row"> 
                    <div className = "bold header"> {item.name} </div>
                    <div> {account[item.key]} </div>
                </div>
              })
            }
        </div>
      }
    </div>
  )
}

export default AccountSummary