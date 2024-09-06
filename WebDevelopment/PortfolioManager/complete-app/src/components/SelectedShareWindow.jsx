export default function SelectedShareWindow({ selectedShare, handleOpenSelectedShareWindow }) {
    return (
      <>
        <div className="border-y border-slate-300 py-4 px-6 py-4">{`${selectedShare["symbol"]}:${selectedShare["name"]}`}</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">${selectedShare["sharePrice"]}</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">---</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">---</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">---</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">---</div>
        <div className="border-y border-slate-300 py-4 px-6 py-4">---</div>
        <div className="border-y border-slate-300 py-4">
          <input className="rounded-full bg-slate-950 text-white text-lg w-1/2 hover:cursor-pointer" type="button" onClick={() => handleOpenSelectedShareWindow()} value="Buy"/>
        </div>
        <div className="border-y border-slate-300 py-4 pr-3"></div>
      </>
    );
}
