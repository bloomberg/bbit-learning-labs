/*
  Copyright 2024 Bloomberg Finance L.P.

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

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
