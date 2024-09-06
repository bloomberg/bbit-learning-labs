export default function ShareSuggestion({ symbol, name, updateShareField, disableShareDropdown, updateSelectedShare }) {
    return (
        <div className="px-5 py-3 text-stone-600 cursor-pointer hover:bg-gray-100 transition-colors" onClick={ () => { updateShareField(symbol); disableShareDropdown(false); updateSelectedShare(symbol, name) } }>{`${symbol}:${name}`}</div>
    );
}
