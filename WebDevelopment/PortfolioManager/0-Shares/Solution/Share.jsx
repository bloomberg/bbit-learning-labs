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

export default function Share() {
    return (
      <>
        <div className="border-y border-black px-6 py-4">MYSHR</div>
        <div className="border-y border-black dollars px-6 py-4">1</div>
        <div className={`border-y border-black  px-6 py-4`}>0.5</div>
        <div className="border-y border-black px-6 py-4">1</div>
        <div className="border-y border-black dollars px-6 py-4">0.7</div>
        <div className="border-y border-black dollars px-6 py-4">1</div>
        <div className="border-y border-black percentage px-6 py-4">0.3</div>
      </>
    );
}
