from importlib.resources import contents
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from pystratis.nodes import StraxNode
from typing import List
from django.contrib.auth.models import User
from pystratis.core.networks import StraxTest
from pystratis.core import Outpoint, Recipient
from pystratis.core.types import Money, Address
from pystratis.api.wallet.responsemodels import SpendableTransactionsModel

def index(request):
    return render(request,'index.html')
def main(request):
    user=str(request.user)
    node=StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=user)
    wallet_balance = node.wallet.balance(
        wallet_name=user,
        include_balance_by_address=False
    )
    balance=wallet_balance.balances[0].amount_confirmed
    unbalance=wallet_balance.balances[0].amount_unconfirmed

    if balance == 0E-8:
        cfm= "0.00000000"
    else :
        cfm=balance

    if unbalance == 0E-8:
        uncfm= "0.00000000"
    else :
        uncfm=unbalance
    return render(request,'main.html',{'add':unused_address,'bal':cfm,'UncBal':uncfm})

def newTxn(request):
    current_user = str(request.user)
    node = StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=current_user)
    wallet_balance = node.wallet.balance(
        wallet_name=current_user,
        include_balance_by_address=False
    )
    balance=wallet_balance.balances[0].amount_confirmed
    unbalance=wallet_balance.balances[0].amount_unconfirmed

    if balance == 0E-8:
        cfm= "0.00000000"
    else :
        cfm=balance

    if unbalance == 0E-8:
        uncfm= "0.00000000"
    else :
        uncfm=unbalance

    if request.method=="POST":
        dest_add = request.POST.get('add')
        amount = request.POST.get('amount')
        name = request.POST.get('name')
        password = request.POST.get('pas')
        user_add = request.POST.get('uradd')
        node = StraxNode(blockchainnetwork=StraxTest())
        s_txs: SpendableTransactionsModel = node.wallet.spendable_transactions(wallet_name=current_user)
        s_txs = [x for x in s_txs.transactions]
        s_txs = sorted(s_txs, key=lambda x: x.amount)
    
        destination_address = Address('qXi54cEGLrZiYJtGt1AipzHMuZEGbbJXYf',StraxTest())
    
    
        change_address = node.wallet.balance(
            wallet_name=current_user, include_balance_by_address=True).balances[0].addresses[0].address
    
    
        fee_amount = Money(0.0001)
        amount_to_send = Money(1)
    
        transactions = []
        trxid_amount = Money(0)
        for spendable_transaction in s_txs:
            transactions.append(spendable_transaction)
            trxid_amount += spendable_transaction.amount
            if trxid_amount >= amount_to_send: 
                break
    
    
        response = node.wallet.build_transaction(
            fee_amount=fee_amount,
            password=password,
            segwit_change_address=False,
            wallet_name=current_user,
            account_name='account 0',
            outpoints=[Outpoint(transaction_id=x.transaction_id, index=x.index) for x in transactions],
            recipients=[Recipient(destination_address=destination_address, subtraction_fee_from_amount=True, amount=amount_to_send)],
            allow_unconfirmed=False,
            shuffle_outputs=True,
            change_address=change_address
        )
    
        response = node.wallet.send_transaction(transaction_hex=response.hex)
        print(response.transaction_id)
        # trxn= response.transaction_id
    
    
    
    return render(request,'newTxn.html',{'add':unused_address,'bal':cfm,'UncBal':uncfm})
def oldTxns(request):
    return render(request,'oldTxns.html')


def profile(request):
    current_user = str(request.user)
    node = StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=current_user)
    wallet_balance = node.wallet.balance(
        wallet_name=current_user,
        include_balance_by_address=False
    )
    balance=wallet_balance.balances[0].amount_confirmed
    unbalance=wallet_balance.balances[0].amount_unconfirmed
    if balance == 0E-8:
        cfm= "0.00000000"
    else :
        cfm=balance
    
    if unbalance == 0E-8:
        uncfm= "0.00000000"
    else :
        uncfm=unbalance
    return render(request,'profile.html',{'add':unused_address,'bal':cfm,'UncBal':uncfm})



def wallet(request):
    current_user = str(request.user)
    node = StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=current_user)
    wallet_balance = node.wallet.balance(
        wallet_name=current_user,
        include_balance_by_address=False
    )
    balance=wallet_balance.balances[0].amount_confirmed
    return render(request,'wallet.html',{'add':unused_address,'bal':balance})


def register(request):
    
    if request.method=="POST":
        username = request.POST.get('name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        pas= request.POST.get('pas')
        pas2 = request.POST.get('pas2')
     
    
        user=User.objects.create_user(username=username,email=email,password=pas,)
        user.save()

        print("user created")
        node = StraxNode(blockchainnetwork=StraxTest())
        mnemonic: List[str] = node.wallet.create(name=username, password=pas, passphrase='') 
             
    
        return redirect("login")
    
    return render(request,"signup.html")


def loginpage(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pwd = request.POST.get('pas')
            
        user = authenticate(request, username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect("main")
        else:
            return redirect("login")
            
    return render(request,"login.html") 
    

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        
    return redirect('login')


def address(request):
    current_user = str(request.user)
    node = StraxNode(blockchainnetwork=StraxTest())
    unused_address = node.wallet.unused_address(wallet_name=current_user)
    return render(request,"address.html",{'address':unused_address})