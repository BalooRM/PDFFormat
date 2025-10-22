function numberFormat(value, decimals = 2, useSeparators = true, currencySymbol = "", symbolBefore = true)  { 
    if (typeof value !== "number" || isNaN(value))  { 
        throw new Error("Invalid number input");
    }
    // Configure number formatting
    const options =  { 
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
        useGrouping: useSeparators
    };
    // Format number
    let formatted = new Intl.NumberFormat("en-US", options).format(value);
    // Add currency symbol if provided
    if (currencySymbol)  { 
        formatted = symbolBefore ? `${currencySymbol}${formatted}` :
          `${formatted}${currencySymbol}`;
    }
    return formatted;
}

function currencyFormat(value, decimals = 2, useSeparators = true, currencySymbol = "$ ", symbolBefore = true)  { 
    if (typeof value !== "number" || isNaN(value))  { 
        throw new Error("Invalid number input");
    }
    // Configure number formatting
    const options =  { 
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
        useGrouping: useSeparators
    };
    // Format number
    let formatted = new Intl.NumberFormat("en-US", options).format(value);
    // Add currency symbol if provided
    if (currencySymbol)  { 
        formatted = symbolBefore ? `${currencySymbol}${formatted}` :
          `${formatted}${currencySymbol}`;
    }
    return formatted;
}

function percentFormat(value, decimals = 2, useSeparators = true, specialSymbol = "%", symbolBefore = false)  { 
    if (typeof value !== "number" || isNaN(value))  { 
        throw new Error("Invalid number input");
    }
    // Configure number formatting
    const options =  { 
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
        useGrouping: useSeparators
    };
    // Format number
    let formatted = new Intl.NumberFormat("en-US", options).format(value);
    // Add currency symbol if provided
    if (specialSymbol)  { 
        formatted = symbolBefore ? `${specialSymbol}${formatted}` :
          `${formatted}${specialSymbol}`;
    }
    return formatted;
}

