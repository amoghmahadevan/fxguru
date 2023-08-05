import React from 'react'

function Select({options, title, name, defaultValue, onSelected}) {

    const handleChange = (e) => {
        onSelected(e.target.value);
    }

    return (
        <div>
            <label htmlFor={name}> {title} </label>
            <select className = "select" name={name} id={name} value={defaultValue} onChange = {(e) => handleChange(e)}>
                {
                    options.map(item => {
                        return <option key={item.key} value={item.value}>
                            {item.text}
                        </option>
                    })
                }
            </select>
        </div>
    )
}

export default Select