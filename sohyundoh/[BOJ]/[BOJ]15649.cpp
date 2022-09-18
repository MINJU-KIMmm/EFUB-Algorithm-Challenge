#include<iostream>
#include<bitset>
#include<vector>
#include<string>

using namespace std;



bitset<9> Combine;
vector<string> SeriesArr{};
int MaxNum = 0;
int SeriesSize = 0;
void ExtractNum(int const ExtractCount = 1, string const& SeriesStr = "")
{

	for (int i = 1; i <= MaxNum; i++)
	{
		string NewSeriesStr = SeriesStr;
		if (Combine[i] == false)
		{
			Combine[i] = true;
			NewSeriesStr = SeriesStr + to_string(i) + " ";
			if (ExtractCount == SeriesSize)
				SeriesArr.push_back(NewSeriesStr);
			else if (ExtractCount < SeriesSize)
				ExtractNum(ExtractCount + 1, NewSeriesStr);
			Combine[i] = false;
		}
	}
}

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	Combine.reset();

	cin >> MaxNum >> SeriesSize;
	ExtractNum();

	for (string const& elem : SeriesArr)
		cout << elem << "\n";

	return 0;
}