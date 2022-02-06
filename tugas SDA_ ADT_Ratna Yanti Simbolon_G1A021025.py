#include <iostream>
using namespace std;
struct pembelian{
   string nama_pembelian;
   string satuan;
   float harga_satuan;
   string nama_kasir;

};
int main() {
    pembelian brg[100];
int no_transaksi,i;
    cout<<"No Transaksi : ";
    cin>>no_transaksi;
    cin.ignore(1000, '\n');


for (i=0;i<no_transaksi;i++){
    cout<<"pembelian ke "<<(i+1)<<endl;
    cout<<"Nama Product : ";
    getline(cin,brg[i].nama_pembelian,'\n');
    cout<<"Satuan : ";
    getline(cin,brg[i].satuan,'\n');
    cout<<"Harga satuan : ";
    cin>>brg[i].harga_satuan;
    cin.ignore(1000, '\n');
    cout<<"Nama kasir : ";
    getline(cin,brg[i].nama_kasir,'\n');
}

for (i=0;i<no_transaksi;i++){
    cout<<brg[i].nama_pembelian<<"\t"<<brg[i].satuan<<"\t";
    cout<<brg[i].harga_satuan<<"\t"<<brg[i].nama_kasir<<endl;
}
return 0;
}