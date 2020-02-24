﻿using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.ComponentModel;
using System.Text;

namespace OpenDL.Model
{
    public class SegmentLabelInfo : INotifyPropertyChanged
    {

        public event PropertyChangedEventHandler PropertyChanged;
        public void OnPropertyRaised(string propertyname)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(propertyname));
            }
        }

        public void Set<T>(string _name, ref T _reference, T _value)
        {
            if (!Equals(_reference, _value))
            {
                _reference = _value;
                OnPropertyRaised(_name);
            }
        }


        public SegmentLabelInfo()
        {
            this.Labels = new ObservableCollection<SegmentationPolygon>();
        }


        private ObservableCollection<SegmentationPolygon> _Labels = null;
        public ObservableCollection<SegmentationPolygon> Labels
        {
            get => _Labels;
            set => Set<ObservableCollection<SegmentationPolygon>>(nameof(Labels), ref _Labels, value);
        }

    }
}