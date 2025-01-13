import pandas as pd


class TimelineRenderer:
    @staticmethod
    def render_html(df: pd.DataFrame) -> str:
        """Generate HTML for the timeline."""
        html = """
        <style>
        body {
          background-color:#1D1D1D;
          min-height:100vh;
          margin:0;
          font-family: 'Droid Sans', sans-serif;
        }
        body:before {
          content: '';
          position: fixed;
          top:0px;
          left:50%;
          bottom:0px;
          transform:translateX(-50%);
          width:4px;
          background-color:#fff;
        }
        .entries {
          width:calc(100% - 80px);
          max-width:800px;
          margin:auto;
          position: relative;
          left:-5px;
        }
        .entry {
          width:calc(50% - 80px);
          float:left; 
          padding:20px;
          clear:both;
          text-align:right;
        }
        .entry:not(:first-child) {
          margin-top:-60px;
        }
        .entry .title {
          font-size:32px;
          margin-bottom:12px;
          position: relative;
          color:#fff;
        }
        .entry .title:before {
          content: '';
          position: absolute;
          width:8px;
          height:8px;
          border:4px solid #ffffff;
          background-color:#1D1D1D;
          border-radius:100%;
          top:50%;
          transform:translateY(-50%);
          right:-73px;
          z-index:1000;
        }
        .entry:nth-child(2n) {
          text-align:left;
          float:right;
        }
        .entry:nth-child(2n) .title:before {
          left:-63px;
        }
        .entry .body {
          color:#aaa;
        }
        .entry .body p {
          line-height:1.4em;
        }
        </style>
        <div class="entries">
        """
        for _, row in df.iterrows():
            html += f"""
            <div class="entry">
                <div class="title">{row['date']}</div>
                <div class="body">
                    <p>{row['description']}</p>
                </div>
            </div>
            """
        html += "</div>"
        return html
